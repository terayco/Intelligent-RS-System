import json
import os

from flask import Blueprint, request, jsonify

from applications.common.curd import model_to_dicts
from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authority
from applications.common.utils import upload as upload_curd
from applications.extensions import db
from applications.models.admin_analysis import AdminAnalysis, AdminNews
from applications.schemas.admin_analysis import AdminNewsSchema

home_api = Blueprint('home_api', __name__, url_prefix='/api/home')

"""
    成果展示



@home_api.get('/')
def show_achievements():
    jsons = load_json()
    for o in jsons:
        title_ = o["title"]
        # words_ = o["words"]
        url_ = o["url"]
        date_ = o["date"]
        news = AdminNews(type=3, title=title_, url=url_, date=json.dumps(date_))
        db.session.add(news)
    db.session.commit()
    return success_api()
"""

@home_api.get('/news')
def show_news():
    _type = request.args.get('type')
    if _type == None or _type == '""' or _type == "":
        log = AdminNews.query.layui_paginate()
        count = log.total
        items = log.items
        dicts = model_to_dicts(schema=AdminNewsSchema, data=items)
        return table_api(data=dicts, count=count)
    else:
        log = AdminNews.query.filter_by(type=_type).layui_paginate()
        count = log.total
        items = log.items
        for t in items:
            ts = t.date.replace("\\", "")
            t.date = json.loads(ts)

        dicts = model_to_dicts(schema=AdminNewsSchema, data=items)
        return table_api(data=dicts, count=count)

    pass


def load_json():
    file_name = r"E:\codedata\waibao\hhu-admin-flask\docs\行业动态.json"
    file_json = {}
    if os.path.exists(file_name):
        with open(file_name, encoding="UTF-8") as file:
            file_json = json.load(file)

    return file_json
