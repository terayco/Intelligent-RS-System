from applications.common.utils import type_utils
from applications.extensions import ma
from marshmallow import fields, validate


class AdminAnalysisSchema(ma.Schema):
    id = fields.Integer()
    uid = fields.Integer()
    type = fields.Integer()
    before_img = fields.Str()
    before_img1 = fields.Str()
    after_img = fields.Str()
    data = fields.Dict()
    is_hole = fields.Boolean()
    create_time = fields.DateTime()


class AdminNewsSchema(ma.Schema):
    id = fields.Integer()
    type = fields.Integer()
    title = fields.Str()
    url = fields.Str()
    words = fields.Str()
    date = fields.Dict()
