from . import Info, RefSchema
from ..extensions import db, ma
from app.exceptions import ValidationError

class General(Info):

    __tablename__ = 'general'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    # cat = db.Column(db.String(25))

    __mapper_args__ = {
        'polymorphic_identity': 'gn'
    }

    def __init__(self):
        pass

    def __repr__(self):
        return "<Model General>"

    def import_data(self, data):
        try:
            self.c_name = data['c_name']
            self.e_name = data['e_name']
            self.type = data['type']
            self.desc = data['desc']
            self.ref_min = float(data['ref_min'])
            self.ref_max = float(data['ref_max'])
        except KeyError as e:
            raise ValidationError("Invalid General: missing " + e.args[0])

class GeneralSchema(ma.ModelSchema):
    refs = ma.Nested(RefSchema, many=True)

    class Meta:
        model = General