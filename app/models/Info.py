from ..extensions import db, ma
from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from . import RefSchema
from . import CRUD
class Info(db.Model, CRUD):
    __tablename__ =  'infos'
    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(255), nullable=True)
    e_name = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    desc = db.Column(db.Text(), nullable=True)
    ref_min = db.Column(db.Float, nullable=True)
    ref_max = db.Column(db.Float, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'info',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }
    refs = db.relationship(
        'Ref',
        backref='info',
        lazy='subquery'
    )

    def __repr__(self):
        return "<Model Info `{}`>".format(self.c_name)


# class InfoSchema(ma.ModelSchema):
#     refs = ma.Nested(RefSchema, many=True)
#     class Meta:
#         model = Info
#
#     @post_dump(pass_many=True)
#     def wrap_if_many(self, data, many=False):
#         if many:
#             return {'infos': data}
#         return data

class InfoSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    c_name = fields.String(validate=not_blank)
    e_name = fields.String(validate=not_blank)

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/infos/"
        else:
            self_link = '/users/{}'.format(data['id'])
        return {'self': self_link}

    class Meta:
        type='info'

