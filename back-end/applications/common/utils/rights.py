import os
from functools import wraps
from flask import abort, request, jsonify, session
from flask_login import login_required
from applications.common.admin_log import admin_log
from applications.common.utils.Jwt import Jwt
from applications.common.utils.code import TAKEN_EXPIRE
from applications.common.utils.http import fail_api


def authorize(power: str, log: bool = False):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session.get('permissions'):
                if log:
                    admin_log(request=request, is_access=False)
                if request.method == 'GET':
                    abort(403)
                else:
                    return jsonify(success=False, msg="权限不足!")
            if log:
                admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def authority(log: bool = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization", None)
            if token == None:
                return fail_api("未登录！", TAKEN_EXPIRE)
            find = token.find("Bearer ")
            if find < 0:
                return fail_api("未登录！", TAKEN_EXPIRE)
            token1 = token[len("Bearer "):len(token)]
            key = os.getenv('SECRET_KEY', '147258369')
            decode = Jwt.decode(token1.encode(), key)
            if decode is None or 'user_id' not in decode or 'user_name' not in decode:
                return fail_api("未登录！", TAKEN_EXPIRE)
            session["_user_id"] = decode['user_id']
            session["user_name"] = decode['user_name']
            if decode == None:
                return fail_api("未登录！", TAKEN_EXPIRE)
            if log:
                admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator
