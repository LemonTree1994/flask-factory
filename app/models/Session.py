import datetime
import random
import string

from app import db

class Session(db.Model):
    __tablename__='session'
    id=db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Integer, db.ForeignKey('user.id'))
    sessionid=db.Column(db.String(64))
    add_date=db.Column(db.DateTime, default=datetime.datetime.now)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Session {}>'.format(self.sessionid)

    def __str__(self):
        return self.__repr__()

    @classmethod
    def get_by_id(cls,sessionid):
        sessions = Session.query.filter_by(sessionid=sessionid, active=True).all()
        if sessions and len(sessions) == 1:
            session = sessions[0]
            if session.add_date + datetime.timedelta(hours=6) > datetime.datetime.now():
                return session

    @classmethod
    def create_session(cls,user):
        sessionid = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        session = Session(userid=user.id, sessionid=sessionid)
        db.session.add(session)
        db.session.commit()
        return sessionid

    @classmethod
    def disable_session(cls,session):
        session = Session.get_by_id(session.sessionid)
        if session:
            session.active = False
            db.session.commit()
        return session