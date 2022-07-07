from applications.common.utils import type_utils
from applications.extensions import ma
from marshmallow import fields


class AdminFeedbackSchema(ma.Schema):
    id = fields.Integer()
    uid = fields.Integer()
    type = fields.Integer()
    analysis_id = fields.Integer()
    content = fields.Str()
    create_time = fields.DateTime()


class AdminFeedbackSchemaPro(ma.Schema):
    id = fields.Integer()
    uid = fields.Integer()
    type = fields.Integer()
    before_img = fields.Str()
    before_img1 = fields.Str()
    after_img = fields.Str()
    content = fields.Str()
    create_time = fields.DateTime()
