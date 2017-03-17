from ..extensions import db, ma
from . import RefSchema, CRUD
from app.exceptions import ValidationError


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

    def import_data(self, data):
        try:
            self.c_name = data['c_name']
            self.e_name = data['e_name']
            self.type = data['type']
            self.desc = data['desc']
            self.ref_min = float(data['ref_min'])
            self.ref_max = float(data['ref_max'])
        except KeyError as e:
            raise ValidationError("Invalid Information: missing " + e.args[0])


class InfoSchema(ma.ModelSchema):
    refs = ma.Nested(RefSchema, many=True)
    class Meta:
        model = Info

    # @post_dump(pass_many=True)
    # def wrap_if_many(self, data, many=False):
    #     if many:
    #         return {'infos': data}
    #     return data


