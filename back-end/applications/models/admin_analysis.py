import datetime
from applications.extensions import db


class AdminAnalysis(db.Model):
    __tablename__ = 'admin_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer)
    type = db.Column(db.Integer)
    before_img = db.Column(db.String(512))
    before_img1 = db.Column(db.String(512))
    after_img = db.Column(db.String(512))
    data = db.Column(db.String(2048))
    is_hole = db.Column(db.Boolean)
    checked = db.Column(db.String(32))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)


class AdminNews(db.Model):
    __tablename__ = 'admin_news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer)
    title = db.Column(db.String(512))
    url = db.Column(db.String(512))
    words = db.Column(db.String(512))
    date = db.Column(db.String())
