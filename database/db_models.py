import datetime
import mongoengine as db
import uuid

DB_URI="mongodb+srv://sid:sidra@cluster0.w19pm.mongodb.net/TweetDetector?retryWrites=true&w=majority"
db.connect(host=DB_URI)

class User(db.Document):
    username = db.StringField(max_length=50,unique=True)
    email = db.StringField(required=True)
    password = db.StringField(max_length=50)

    def to_json(self):
        return{
            'username': self.username,
            'email':self.email,
            'password':self.password,
        }

class Tweets(db.Document):   
    postId =db.StringField(required=True)
    url = db.StringField(required= True)
    text = db.StringField(required= True)
    scaled_image = db.StringField(required= True)
    validation = db.StringField(required= True)
    date = db.StringField(required=True)
    username = db.StringField(required=True)
    screen_name = db.StringField(required=True)
    created_date = db.StringField(required=True)
    followings = db.IntField(required=True)
    followers = db.IntField(required=True)
    likes = db.IntField(required=True)

    def to_json(self):
        return{
            'postId':self.postId,
            'url': self.url,
            'text':self.text,
            'scaled_image':self.scaled_image,
            'validation':self.validation,
            'date':self.date,
            'username':self.username,
            'screen_name':self.screen_name,
            'created_date':self.created_date,
            'followings':self.followings,
            'followers':self.followers,
            'likes':self.likes
        }
