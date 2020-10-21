from flask import Flask, request, jsonify, Response
import datetime
import my_main as m
import database.db_models as db_models
from flask_cors import CORS
import json
import uuid
app = Flask(__name__)
CORS(app)

# register a user
@app.route("/api/register", methods=["POST"])
def register():
    requestData = request.get_json()
    try:
        user = db_models.User(**requestData).save()
        return jsonify({"user": user.to_json(), "message": "Registered Successfully", "status": 200})
    except:
        return jsonify({"message": "Username already taken", "status": 400})

# login user
@app.route("/api/login", methods=["POST"])
def login():
    requestData = request.get_json()
    userObject = db_models.User.objects.get(
        username=requestData['username'], password=requestData['password']).to_json()
    if userObject:
        print(userObject)
        return jsonify(userObject)
    else:
        return jsonify({"error_message": "Invalid Credentials", "status": 400})

# get all validated tweets of a user
@app.route("/api/tweets/all/<username>", methods=['GET'])
def getAllUserPostHistory(username):
    postList = db_models.Tweets.objects(username=username).all().to_json()
    lists = json.dumps(postList)
    print(postList)
    if postList:
        return postList
    else:
        return jsonify({"message": "Empty History", "status": 200})

# get a particular validated post of a user
@app.route("/api/getAPost/<postId>", methods=['GET'])
def getAPost(postId):
    post = db_models.Tweets.objects.get(id=postId).to_json()
    print(post)
    if post:
        return post
    else:
        return jsonify({"message": "Id not availabel", "status": 404})


# //gets the tweet details no validation
@app.route("/api/check-tweet/<username>/<postId>", methods=['GET'])
def validateTweet(username, postId):
    final_result = m.validate_tweet_text(postId)
    print(final_result)
    if final_result == '0':
        validate='Fake'
        print("Fake")
    else:
        validate='True'
        print("True")
    # get the tweet data
    now = datetime.datetime.now()
    current_date = now.strftime("%Y/%m/%d %H:%M:%S")
    data = m.tweet_data_retrievel(postId)
    screenname = data['screen_name']
    data['username'] = username
    data['url'] = "https://twitter.com/"+screenname+"/status/"+postId
    data['validation'] = validate #assign the result to the validation
    data['date'] = current_date
    tweet = db_models.Tweets(**data).save()
    return jsonify({"tweet": tweet.to_json(), "message": "Successfully validated", "status": 200})


@app.route("/api/check-model/<username>/<postId>", methods=['GET'])
def validateTweetCheck(username, postId):
    final_result = m.validate_tweet_text(postId)
    print(final_result)
    if final_result == '0':
        validate='false'
        print("false")
    else:
        validate='true'
        print("true")
    now = datetime.datetime.now()
    current_date = now.strftime("%Y/%m/%d %H:%M:%S")
    data = m.tweet_data_retrievel(postId)
    screenname = data['screen_name']
    data['username'] = username
    data['url'] = "https://twitter.com/"+screenname+"/status/"+postId
    data['validation'] = validate #assign the result to the validation
    data['date'] = current_date
    tweet = db_models.Tweets(**data).save()
    return jsonify({"tweet": tweet.to_json(), "message": "Successfully validated", "status": 200})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
