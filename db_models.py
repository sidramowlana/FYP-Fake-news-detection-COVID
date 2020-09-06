import datetime
import mongoengine as db

DB_URI="mongodb+srv://sid:sidra@cluster0.w19pm.mongodb.net/TweetDetector?retryWrites=true&w=majority"
db.connect(host=DB_URI)
# connect('mongoengine_test', host='localhost', port=27017)

class User(db.Document):
    username = db.StringField(max_length=50,unique=True)
    email = db.StringField(required=True)
    password = db.StringField(max_length=50)

    def to_json(self):
        return{
            'username': self.username,
            'email':self.email,
            'password':self.password
        }


class TweetDetector(db.Document):
    url = db.StringField(required= True)
    text = db.StringField(required= True)
    percentage = db.IntField(required= True)

    def to_json(self):
        return{
            'url': self.url,
            'text':self.text,
            'percentage':self.percentage
        }

# ross = User(username='ross@example.com', email='Ross', password='Lawley').save()
# print(ross)

