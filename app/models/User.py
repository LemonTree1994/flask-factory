import datetime
from app import db

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    active = db.Column(db.Boolean, default=True)
    sessions = db.relationship("Session", backref="user_from_session")  # backref:

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __str__(self):
        return self.__repr__()

    @classmethod
    def validate_user(cls,username, password):
        users = User.query.filter_by(username=username, password=password).all()
        if users and len(users) == 1:
            user = users[0]
            return user

    @classmethod
    def name_is_exist(cls,username):
        users = User.query.filter_by(username=username).all()
        if users and len(users) > 0:
            return True
        return False

    @classmethod
    def add_user(cls,user):
        db.session.add(user)
        db.session.commit()
        return User.validate_user(user.username, user.password)