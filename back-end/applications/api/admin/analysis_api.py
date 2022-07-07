import json

from flask import Blueprint, request, jsonify, session, current_app
from sqlalchemy import desc

from applications.common.curd import model_to_dicts
from applications.common.path_global import up_dir, generate_dir, fun_type_1, fun_type_4, fun_type_5, fun_type_3, \
    fun_type_2, generate_url
from applications.common.utils import type_utils
from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authority
from applications.common.utils.type_utils import items_handle
from applications.common.utils.upload import img_url_handle
from applications.extensions import db
from applications.image_processing import histogram_match
from applications.models.admin_analysis import AdminAnalysis
from applications.models.admin_feedback import AdminFeedback
from applications.rs.analysis import change_detection, object_detection, segmenter, terrain_classification, hole_handle, \
    handle
from applications.schemas import AdminAnalysisSchema
from applications.schemas.admin_feedback import AdminFeedbackSchemaPro

analysis_api = Blueprint('analysis_api', __name__, url_prefix='/api/analysis')

"""
    结果展示
"""


@analysis_api.get('/show/<string:type>')
@authority(log=True)
def show_result(type):
    # orm查询
    # 使用分页获取data需要.items
    to_type = type_utils.str_to_type(type)
    log = AdminAnalysis.query.filter_by(type=to_type).order_by(desc(AdminAnalysis.create_time)).layui_paginate()
    log_items = log.items
    items_handle(log_items)
    count = log.total
    return table_api(data=model_to_dicts(schema=AdminAnalysisSchema, data=log_items), count=count)


@analysis_api.post('/feedback')
@authority(log=True)
def feedback():
    req_json = request.json
    type_ = req_json['type']
    type_ = type_utils.str_to_type(type_)
    analysis_id_ = req_json['analysis_id']
    content_ = req_json['content']
    if type_ is None or analysis_id_ is None or content_ is None:
        return fail_api("参数异常")

    count = AdminAnalysis.query.filter_by(id=analysis_id_).count()
    if count <= 0:
        return fail_api("这一组分析记录不存在")
    if len(content_) == 0:
        return fail_api("请填写反馈内容")
    feedback = AdminFeedback()
    feedback.type = type_
    feedback.uid = session.get('_user_id')
    feedback.analysis_id = analysis_id_
    feedback.content = content_
    db.session.add(feedback)
    db.session.commit()
    return success_api(msg="反馈成功")


@analysis_api.get('/feedback/list')
@authority(log=True)
def feedback_list():
    uid = session.get('_user_id')
    user_name_ = session["user_name"]
    # orm查询
    # 使用分页获取data需要.items
    if user_name_=="admin":
        sql = f"SELECT af.id,content,aa.type,af.uid,before_img,before_img1,after_img,af.create_time,aa.is_hole,aa.data  FROM `admin_feedback` af INNER JOIN `admin_analysis` aa ON aa.`id`=af.`analysis_id`  LIMIT {request.args.get('page', type=int) - 1},{request.args.get('limit', type=int)}"
    else:
        sql = f"SELECT af.id,content,aa.type,af.uid,before_img,before_img1,after_img,af.create_time,aa.is_hole,aa.data  FROM `admin_feedback` af INNER JOIN `admin_analysis` aa ON aa.`id`=af.`analysis_id` where af.uid={uid} LIMIT {request.args.get('page', type=int) - 1},{request.args.get('limit', type=int)}"
    lists = db.session.execute(sql).fetchall()
    items = model_to_dicts(schema=AdminFeedbackSchemaPro, data=lists)
    if user_name_ == "admin":
        sql1 = f"SELECT COUNT(1) FROM `admin_feedback` af INNER JOIN `admin_analysis` aa ON aa.`id`=af.`analysis_id`"
    else:
        sql1 = f"SELECT COUNT(1) FROM `admin_feedback` af INNER JOIN `admin_analysis` aa ON aa.`id`=af.`analysis_id` where af.uid={uid}"
    fetchone = db.session.execute(sql1).fetchone()
    items_handle(items)
    return table_api(data=items, count=fetchone[0])


"""
    变化检测
"""


@analysis_api.post('/change_detection')
@authority(log=True)
def change_detection_api():
    req_json = request.json
    uid = session.get('_user_id')
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    step2_ = req_json["denoise"]
    if step1_ is None or step1_ is None or step1_ not in (0, fun_type_1, fun_type_4) or step2_ not in (
            0, fun_type_3, fun_type_5):
        return fail_api("参数异常")
    if list_ is None:
        return fail_api("请上传图片")

    for pair in list_:
        if "first" not in pair or "second" not in pair or pair["first"] == "" or pair["second"] == "":
            return fail_api("请求参数异常")
    print("----------------->change_detection"+json.dumps(req_json))
    type_ = 1
    change_detection("RS/static_models/ChangeDetection256x256", up_dir, generate_dir, list_, step1_, step2_, uid, type_)
    return success_api()


"""
    目标检测
"""


@analysis_api.post('/object_detection')
@authority(log=True)
def object_detection_api():
    req_json = request.json
    uid = session.get('_user_id')
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    step2_ = req_json["denoise"]
    if step1_ is None or step1_ is None or step1_ not in (0, fun_type_2, fun_type_4) or step2_ not in (
            0, fun_type_3, fun_type_5):
        return fail_api("参数异常")
    if list_ is None:
        return fail_api("请上传图片")
    type_ = 2
    object_detection("RS/static_models/ObjectDetection608x608", up_dir, generate_dir, list_, step1_, step2_, uid, type_)

    return success_api()


"""
    目标提取
"""


@analysis_api.post('/object_extraction')
@authority(log=True)
def object_extraction_api():
    req_json = request.json
    uid = session.get('_user_id')
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    step2_ = req_json["denoise"]
    if step1_ is None or step1_ is None or step1_ not in (0, fun_type_2, fun_type_4) or step2_ not in (
            0, fun_type_3, fun_type_5):
        return fail_api("参数异常")
    if list_ is None:
        return fail_api("请上传图片")
    type_ = 3
    segmenter("RS/static_models/Segmenter128x128", up_dir, generate_dir, list_, step1_, step2_, uid, type_)
    return success_api()


"""
    地物分类
"""


@analysis_api.post('/feature_classification')
@authority(log=True)
def feature_classification_api():
    req_json = request.json
    uid = session.get('_user_id')
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    step2_ = req_json["denoise"]
    if step1_ is None or step1_ is None or step1_ not in (0, fun_type_2, fun_type_4) or step2_ not in (
            0, fun_type_3, fun_type_5):
        return fail_api("参数异常")
    if list_ is None:
        return fail_api("请上传图片")
    type_ = 4
    terrain_classification("RS/static_models/TerrainClassification256x256", up_dir, generate_dir, list_, step1_, step2_,
                           uid, type_)
    return success_api()


"""
    直图处理
"""


@analysis_api.post('/histogram_match')
@authority(log=True)
def pre_handle():
    req_json = request.json
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    if list_ is None:
        return fail_api("请上传图片")
    if step1_ not in (1, 4):
        return fail_api("请求参数异常")
    for pair in list_:
        if "first" not in pair or "second" not in pair or pair["first"] == "" or pair["second"] == "":
            return fail_api("请求参数异常")
        pair["first"] = img_url_handle(pair["first"])
        pair['second'] = img_url_handle(pair['second'])
    match = list()
    if step1_ == fun_type_1:
        match = histogram_match.gram_match(list_, up_dir, generate_dir)
    else:
        for pair in list_:
            temps = [pair["first"], pair["second"]]
            imgs1 = handle(fun_type_4, temps, up_dir, generate_dir)
            match.append({"first": generate_url + imgs1[0], "second": generate_url + imgs1[1]})
    return success_api(data=match)


@analysis_api.post('/image_pre')
@authority(log=True)
def image_pre():
    req_json = request.json
    list_ = req_json["list"]
    step1_ = req_json["prehandle"]
    type = req_json["type"]
    if list_ is None:
        return fail_api("请上传图片")
    if step1_ not in (2, 4):
        return fail_api("请求参数异常")
    imgs = list()
    if type == 1:
        for pair in list_:
            if "first" not in pair or "second" not in pair or pair["first"] == "" or pair["second"] == "":
                return fail_api("请求参数异常")
        for pair in list_:
            temps = [img_url_handle(pair["first"]), img_url_handle(pair["second"])]
            imgs1 = handle(fun_type_4, temps, up_dir, generate_dir)
            imgs.append({"first": pair["first"], "first1": imgs1[0], "second": pair["second"], "second1": imgs1[1]})
    else:
        temps = list()
        for pair in list_:
            temps.append(img_url_handle(pair))
        imgs = handle(step1_, temps, up_dir, generate_dir)
        for i, img in enumerate(imgs):
            imgs[i] = generate_url + img
    return success_api(data=imgs)


"""
    孔洞处理
"""


@analysis_api.post('/hole')
@authority(log=True)
def hole_handle1():
    req_json = request.json
    analysis_id = req_json["id"]
    if analysis_id is None:
        return fail_api("参数异常")

    analysis = AdminAnalysis.query.filter_by(id=analysis_id, type=1).first()
    if not analysis:
        return fail_api("这一组分析记录不存在")
    if analysis.type != 1:
        return fail_api("类型错误")
    if analysis.is_hole:
        return fail_api("这一组分析记录已经孔洞处理过")
    temps = list()
    temps.append(analysis.after_img)
    after_img, data = hole_handle(generate_dir, generate_dir, temps)
    AdminAnalysis.query.filter_by(id=analysis_id).update({"after_img": after_img, "data": data, "is_hole": True})
    db.session.commit()
    return success_api()


def saveAnalysis(uid, type_, pic1, retPic, pic2="", data="{}", is_hole=False):
    analysis = AdminAnalysis()
    analysis.uid = uid
    analysis.type = type_
    analysis.before_img = pic1
    analysis.before_img1 = pic2
    analysis.after_img = retPic
    analysis.data = data
    analysis.is_hole = is_hole
    db.session.add(analysis)
    db.session.commit()
