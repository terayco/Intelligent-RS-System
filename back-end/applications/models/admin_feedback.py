import datetime
from applications.extensions import db


class AdminFeedback(db.Model):
    __tablename__ = 'admin_feedback'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer)
    type = db.Column(db.Integer)
    analysis_id = db.Column(db.Integer)
    content = db.Column(db.String(1024))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
