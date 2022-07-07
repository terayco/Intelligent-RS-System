from applications.extensions import ma
from marshmallow import fields


# 用户models的序列化类
class UserOutSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str()
    realname = fields.Str()
    email = fields.Str()
    enable = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()
