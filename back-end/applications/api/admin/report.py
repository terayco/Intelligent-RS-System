from flask import Blueprint, request, jsonify, session

from applications.common.curd import model_to_dicts
from applications.common.utils.http import fail_api, success_api
from applications.common.utils.rights import authority
from applications.common.utils import upload as upload_curd
from applications.common.utils.type_utils import items_handle
from applications.extensions import db
from applications.models import AdminLog, Photo, User
from applications.schemas.common import SevenDaySchema, FunctionGroupSchema, GroupSchema

report_api = Blueprint('report_api', __name__, url_prefix='/api/report')


def action_report():
    pass


@report_api.get('/')
@authority(log=True)
def report():
    # 总访问量
    visit_count = AdminLog.query.count()
    # 总上传图片数
    photo_count = Photo.query.count()
    # 总注册数
    user_count = User.query.count()

    # 七日访问量
    seven_days_items = db.session.execute(
        "SELECT DATE_FORMAT(create_time, '%Y-%m-%d') dates, COUNT(1) num FROM `admin_admin_log` WHERE create_time > (DATE_SUB( CURDATE(), INTERVAL 7 DAY ))  GROUP BY DATE_FORMAT(create_time, '%Y-%m-%d')").fetchall()

    seven_days_items = model_to_dicts(schema=SevenDaySchema, data=seven_days_items)

    # 各个界面访问量
    function_items = db.session.execute(
        "SELECT url function,COUNT(1) num FROM `admin_admin_log` GROUP BY url").fetchall()

    function_items = model_to_dicts(schema=FunctionGroupSchema, data=function_items)

    statistic = statistics(function_items)

    # 功能区图片上传量
    photo_items = db.session.execute("SELECT TYPE type,COUNT(1) num FROM `admin_photo` GROUP BY TYPE").fetchall()
    photo_items = model_to_dicts(schema=GroupSchema, data=photo_items)
    items_handle(photo_items)

    # 反馈分区数量
    feedback_items = db.session.execute("SELECT TYPE type,COUNT(1) num FROM `admin_feedback` GROUP BY TYPE").fetchall()

    feedback_items = model_to_dicts(schema=GroupSchema, data=feedback_items)
    items_handle(feedback_items)

    data = {
        'visit_count': visit_count,
        'photo_count': photo_count,
        'user_count': user_count,
        'seven_days_items': seven_days_items,
        'function_items': statistic,
        'photo_items': photo_items,
        'feedback_items': feedback_items,
        'user_name': session["user_name"]
    }

    return success_api(data=data)


def statistics(function_items):
    statistics = list()
    fun_filter = [
        {
            "name": "登陆注册",
            "path": ["/api/user/login", "/api/user/register"]
        },
        {
            "name": "变化检测",
            "path": ["/api/analysis/change_detection"]
        },
        {
            "name": "目标监测",
            "path": ["/api/analysis/object_detection"]
        },
        {
            "name": "目标提取",
            "path": ["/api/analysis/object_extraction"]
        },
        {
            "name": "地物分类",
            "path": ["/api/analysis/feature_classification"]
        },
        {
            "name": "我的历史记录",
            "path": ["/api/history/list"]
        },
        {
            "name": "我的反馈记录",
            "path": ["/api/analysis/feedback/list"]
        }
    ]
    for f in fun_filter:
        num = 0
        for item in function_items:

            if f["path"].count(item['function']) > 0:
                num = item['num'] + num

            pass
        statistics.append({"name": f['name'], "num": num})
        pass
    return statistics
