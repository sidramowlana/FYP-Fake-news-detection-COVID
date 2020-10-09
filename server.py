from flask import Flask, request, jsonify, Response
import datetime
import my_main as m
import database.db_models as db_models
from flask_cors import CORS
import json
import uuid
app = Flask(__name__)
CORS(app)


@app.route("/api/register", methods=["POST"])
def register():
    requestData = request.get_json()
    print(requestData)
    try:
        user = db_models.User(**requestData).save()
        return jsonify({"user": user.to_json(), "message": "Registered Successfully", "status": 200})
    except:
        return jsonify({"error_message": "Username already taken", "status": 400})


@app.route("/api/login", methods=["POST"])
def login():
    requestData = request.get_json()
    userObject = db_models.User.objects.get(username=requestData['username'], password=requestData['password']).to_json()    
    if userObject:
        print(userObject)
        return jsonify(userObject)
    else:
        return jsonify({"error_message": "Invalid Credentials", "status": 400})


# get all validated tweets of a user
@app.route("/api/tweets/all/<username>",methods=['GET'])
def getAllUserPostHistory(username):
    postList = db_models.Tweets.objects(username=username).all().to_json()
    lists = json.dumps(postList)
    print(postList)
    if postList:
        return postList
    else:
        return jsonify({"message": "Empty History", "status": 200})


@app.route("/api/getAPost/add", methods=['GET'])
def getAddPost():
    print("")
    requestData = request.get_json()
    print(requestData)
    user = db_models.Tweets(**requestData).save()
    print(str(user['id']))
    return "hii"

# get a particular validated post of a user
@app.route("/api/getAPost/<userid>/<postid>", methods=['GET'])
def getAPost(userid, postid):
    post = db_models.Tweets.objects(userid=userid, postid=postid).get().to_json()
    print(post)
    return "hii"

@app.route("/api/getAllUser", methods=['GET'])
def getAllUser():
    users = db_models.User.objects.to_json()
    print(users)
    return "ok"

@app.route("/api/check-tweet/<username>/<postId>", methods=['GET'])
def validateTweet(username,postId):
    print(username)
    # pass the value to the model and get the percentage value
    now = datetime.datetime.now()
    current_date = now.strftime("%Y/%m/%d %H:%M:%S")
    data = m.get_validated_tweet_data(postId)
    screenname=data['screen_name']
    data['username']=username
    data['url']="https://twitter.com/"+screenname+"/status/"+postId
    data['percentage']=20
    data['date']=current_date
    tweet = db_models.Tweets(**data).save()
    return jsonify({"tweet": tweet.to_json(), "message": "Successfully validated", "status": 200})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
