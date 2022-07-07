import json

from flask import Blueprint, request, jsonify, session
from sqlalchemy import desc

from applications.common.curd import model_to_dicts
from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authority
from applications.common.utils import upload as upload_curd, type_utils
from applications.common.utils.type_utils import items_handle
from applications.extensions import db
from applications.models.admin_analysis import AdminAnalysis
from applications.schemas import AdminAnalysisSchema

history_api = Blueprint('history_api', __name__, url_prefix='/api/history')

"""
    查询我的历史记录
"""


@history_api.get('/list')
@authority(log=True)
def history_list():
    # orm查询
    # 使用分页获取data需要.items
    user_id_ = session["_user_id"]
    _type = request.args.get('type', type=str)
    if _type == None or _type == '""' or _type == "":
        log = AdminAnalysis.query.filter_by(uid=user_id_).order_by(desc(AdminAnalysis.create_time)).layui_paginate()
        count = log.total
        items = log.items
        analysis_handle(items)
        dicts = model_to_dicts(schema=AdminAnalysisSchema, data=items)
        items_handle(dicts)
        return table_api(data=dicts, count=count)
    else:
        to_type = type_utils.str_to_type(_type)
        log = AdminAnalysis.query.filter_by(type=to_type, uid=user_id_).order_by(
            desc(AdminAnalysis.create_time)).layui_paginate()
        count = log.total
        items = log.items
        analysis_handle(items)
        dicts = model_to_dicts(schema=AdminAnalysisSchema, data=items)
        items_handle(dicts)
        return table_api(data=dicts, count=count)


def analysis_handle(items):
    for t in items:
        if t.data == "" or t.data is None:
            continue
        t.data = json.loads(t.data)
    pass


"""
批量删除
"""


@history_api.delete('/batchRemove')
@authority(log=True)
def history_delete():
    req_json = request.json
    if 'ids' in req_json:
        ids = req_json['ids']
        for id in ids:
            res = AdminAnalysis.query.filter_by(id=id).delete()
            db.session.commit()
        return success_api(msg="批量删除成功")
    return fail_api(msg="参数异常")
    pass
