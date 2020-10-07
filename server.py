from flask import Flask, request, jsonify, Response
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


@app.route("/api/tweets/all/<username>",methods=['GET'])
def getAllUserPostHistory(username):
    # postList = db_models.Tweets.objects(username=username).all().to_json()
    postList = db_models.Tweets.objects(username=username).all().to_json()
    lists = json.dumps(postList)
    print(postList)
    #print(lists)
    if postList:
        return postList
    else:
        return jsonify({"message": "Empty History", "status": 200})


@app.route("/api/getAPost/add", methods=['POST'])
def getAddPost():
    print("")
    requestData = request.get_json()
    print(requestData)
    user = db_models.Tweets(**requestData).save()
    print(str(user['id']))
    return "hii"


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

@app.route("/check-tweet", methods=['GET'])
def validateTweet():
    print("started")
    url = request.args['url']
    validated_result = m.validate_tweet_url(url)
    print(validated_result)
    # save the url and the validity in the table
    return "h1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# https://docs.google.com/forms/d/1xkSHVYLVuHrKvZPggNXY9puLmb8JrK_wyE3uO5eeQPI/edit#responses
