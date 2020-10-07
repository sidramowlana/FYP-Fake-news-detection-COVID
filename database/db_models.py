
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
    url = db.StringField(required= True)
    text = db.StringField(required= True)
    scaledImage = db.StringField(required= True)
    percentage = db.IntField(required= True)
    date = db.StringField(required=True)
    username = db.StringField(required=True)

    def to_json(self):
        return{
            'id':str(self.pk),
            'url': self.url,
            'text':self.text,
            'scaledImage':self.scaledImage,
            'percentage':self.percentage,
            'date':self.date,
            'username':self.username
        }