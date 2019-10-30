from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# friends = db.Table('friends',  
#     db.Column('followers', db.Integer, db.ForeignKey('user.id')),
#     db.Column('followed', db.Integer, db.ForeignKey('user.id'))
# )
class User(UserMixin,  db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True, )
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Todo', backref='user', lazy='dynamic')
    # followed=db.relationship('User', secondary=friends,
    #  primaryjoin=(friends.c.followers == id), 
    #  secondaryjoin=(friends.c.followed==id), 
    #  backref=db.backref('friends', lazy='dynamic'), lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Todo(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable = False)
    timestamp = db.Column(db.DateTime, index =True,  default=datetime.utcnow)
    # deadline_date = db.Column(db.Date, index = True, nullable = False)
    # deadline_time = db.Column(db.Time, index = True, nullable = False)
    deadline = db.Column(db.DateTime, index = True, nullable = False)
    status = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Todo {}>'.format(self.description)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
