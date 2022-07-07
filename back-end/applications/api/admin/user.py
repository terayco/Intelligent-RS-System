import os
import time
from datetime import timedelta

from flask import request, Blueprint, session
from flask_login import login_user
from werkzeug.security import generate_password_hash

from applications.common.admin_log import login_log, admin_log
from applications.common.curd import model_to_dicts
from applications.common.helper import ModelFilter
from applications.common.utils.Jwt import Jwt
from applications.common.utils.http import fail_api, success_api, table_api
from applications.common.utils.rights import authority
from applications.common.utils.validate import xss_escape
from applications.extensions import db
from applications.models import User
from applications.schemas import UserOutSchema

user_api = Blueprint('user', __name__, url_prefix='/api/user')


@user_api.post('/login')
def login_post():
    req_json = request.json
    username = req_json.get('username')
    password = req_json.get('password')
    if not username or not password:
        return fail_api(msg="用户名或密码没有输入")

    user = User.query.filter_by(username=username).first()

    if not user:
        return fail_api(msg="不存在的用户")

    if username == user.username and user.validate_password(password):
        # 登录
        login_user(user)
        # 记录登录日志
        login_log(request, uid=user.id, is_access=True)
        # 存入权限
        session["user_id"] = user.id
        key = os.getenv('SECRET_KEY', '147258369')
        token = Jwt.encode({"user_id": user.id, "user_name": user.username}, key, 21600).decode()
        session["accessToken"] = token
        session["_user_id"] = user.id
        admin_log(request=request, is_access=True)
        admin = ""
        if username == "admin":
            admin = username
        return success_api(msg="登录成功", data={"accessToken": token, "superAdmin": admin})
    login_log(request, uid=user.id, is_access=False)
    return fail_api(msg="用户名或密码错误")


@user_api.post('/register')
def save():
    req_json = request.json
    username = xss_escape(req_json.get('username'))
    real_name = username
    password = xss_escape(req_json.get('password'))
    email = xss_escape(req_json.get('email'))

    if not username or not real_name or not password:
        return fail_api(msg="账号姓名密码不得为空")

    if not email:
        return fail_api(msg="邮箱不得为空")

    if bool(User.query.filter_by(username=username).count()):
        return fail_api(msg="用户已经存在")
    user = User(username=username, realname=real_name)
    user.set_password(password)
    user.email = email
    db.session.add(user)
    db.session.commit()
    session["_user_id"] = user.id
    admin_log(request=request, is_access=True)
    return success_api(msg="增加成功")


# 退出登录
@user_api.post('/logout')
def logout():
    if '_user_id' in session:
        session.pop('_user_id')
    return success_api(msg="注销成功")


#   用户分页查询
@user_api.get('/list')
@authority(log=True)
def data():
    # 获取请求参数
    username = xss_escape(request.args.get('username', type=str))
    # 查询参数构造
    mf = ModelFilter()
    if username and username != "":
        mf.contains(field_name="username", value=username)
    # orm查询
    # 使用分页获取data需要.items
    user = User.query.filter(mf.get_filter(model=User)).layui_paginate()
    count = user.total
    # 返回api
    return table_api(data=model_to_dicts(schema=UserOutSchema, data=user.items), count=count)


# 删除用户
@user_api.delete('/remove')
@authority(log=True)
def delete():
    userId = request.args.get('userId')
    if userId == "" or userId is None:
        return fail_api(msg="删除失败")
    res = User.query.filter_by(id=userId).delete()
    db.session.commit()
    if not res:
        return fail_api(msg="删除失败")
    return success_api(msg="删除成功")


@user_api.delete('/batchRemove')
@authority(log=True)
def history_delete():
    req_json = request.json
    if 'userIds' in req_json:
        ids = req_json['userIds']
        for id in ids:
            res = User.query.filter_by(id=id).delete()
            db.session.commit()
        return success_api(msg="批量删除成功")
    return fail_api(msg="参数异常")


#  修改用户密码
@user_api.post('/resetPwd')
@authority(log=True)
def resetPwd():
    req_json = request.json
    id = req_json.get("userId")
    password = xss_escape(req_json.get('newpassword'))
    User.query.filter_by(id=id).update({"password_hash": generate_password_hash(password)})
    db.session.commit()
    return success_api(msg="更新成功")


@user_api.post('/forget')
def forget():
    req_json = request.json
    username = xss_escape(req_json.get('username'))
    password = xss_escape(req_json.get('newPassword'))
    email = xss_escape(req_json.get('myemail'))
    if not username or not password:
        return fail_api(msg="用户名或密码没有输入")
    if not email:
        return fail_api(msg="邮箱不得为空")
    user = User.query.filter_by(username=username, email=email).first()
    if not user:
        return fail_api(msg="不存在的用户")
    #id = req_json.get("userId")
    #password = xss_escape(password)
    User.query.filter_by(id=user.id).update({"password_hash": generate_password_hash(password)})
    db.session.commit()
    return success_api(msg="更新成功")
