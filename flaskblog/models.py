from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin

# this is used for reloading the user from the user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    # get user by its id
    return User.query.get(int(user_id))


# db provides Model that allows us to use class to handle db tables
# each class is going to be its own table in sqlalchemy db
class User(db.Model, UserMixin):
    # as this is a primary key it is set automatically to unique value by Sqlalchemy
    id = db.Column(db.Integer, primary_key=True)        # setting column id of type integer and making it a primary key by setting primary_key contraint to True
    # user column - type string, unique contraint is True (username must be unique) and nullable contraint is False (cannot be empty)
    username = db.Column(db.String(20), unique=True, nullable=False)    
    email = db.Column(db.String(120), unique=True, nullable=False)
    # user dp column, the image will be hashed to string of 20 characters, it cannot be empty though they can have same dp, if nothing is set then a default dp is set for that user
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # this creates a relationship of User object with Post object... backref adds another column (not actually) to User table with name author, that refers to the user itself whenever new # post is 
    # uploaded it will backref author to user posting it to get username as author. lazy attrb just defines when SQLAlchemy loads the data from the db. so lazy=True SQLAlchemy will load
    #  the data in one go... so with this relationship we will able to get all the posts posted by a user 
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        # secret key and expiration time
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # return token
        return s.dumps({'user_id': self.id}).decode('utf-8')
        
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # date posted column is of type datetime and if nothing is set then we will fetch current datetime to do so we have passed only the func name to use it later
    # utcnow time is used in db so as to stay consistent with utc time
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # this creates a user_id column of type integer and its a foreignkey that refers back to the id of user in user db
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
    
# u can see post class doesnt have an author attribute this is coz the user is going to author the post.. so there is a relationship between User and Post db class (db table Model) 
# User-Post has a one-to-many relationship, coz user (is an author) can post multiple posts but one post can have only one author posting   
    