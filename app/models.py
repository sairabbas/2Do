from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True,)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship("Todo", backref="user", lazy="dynamic")
    newTasks = db.relationship("newList", backref="user", lazy="dynamic")

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Todo(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # title to the task
    description = db.Column(db.String(250), index=True, nullable=False)
    # content to the task
    content = db.Column(db.UnicodeText, index=True)
    # time task created
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # time deadline to the task
    deadline = db.Column(db.DateTime, index=True, nullable=False)
    # the status of the task finished or not
    status = db.Column(db.Boolean, default=False)
    # status share
    statusShare = db.Column(db.Boolean, default=False)
    # linking to the user id
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Todo {}>".format(self.description)


class newList(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
