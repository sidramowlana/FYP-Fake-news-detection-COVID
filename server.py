from flask import Flask, request, jsonify, Response
import my_main as m
import db_models
app = Flask(__name__)



@app.route("/register",methods=["POST"])
def register():
    requestData = request.get_json()
    print(requestData)
    try:
        user = db_models.User(**requestData).save()
        return jsonify({"user":user.to_json(),"message":"Registered Successfully","status":200})
    except:
        return jsonify({"message":"Username already taken","status":400})
   
  

@app.route("/login",methods=["GET"])
def login():
    requestData = request.get_json()
    try:        
        userObject= db_models.User.objects.get(username=requestData['username'],password=requestData['password']).to_json()
        return jsonify({"user":userObject,"message":"User Successfuly Logged in","status":200})
    except:
        return jsonify({"message":"Invalid Credentials","status":400})

    
# @app.route("/check-tweet",methods=['GET'])
# def validateTweet():    
#     print("starte")
#     requestData = request.get_json()
#     url = requestData['url']
#     validated_result = m.validate_tweet_url(url)    
#     print(validated_result)
#     return "hi"
    # get the tweet url 
    # check with the model
    # send the validated result
    # def getUserValidatedTweets()

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")