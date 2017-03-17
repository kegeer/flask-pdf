from . import Info, CRUD, RefSchema
from ..extensions import db, ma
from app.exceptions import ValidationError

class Metabolism(Info, CRUD):

    __tablename__ = 'metabolism'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    cat = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'me'
    }

    def __repr__(self):
        return "<Model Metabolism `{}`>".format(self.cat)

    def import_data(self, data):
        try:
            self.c_name = data['c_name']
            self.e_name = data['e_name']
            self.type = data['type']
            self.desc = data['desc']
            self.ref_min = float(data['ref_min'])
            self.ref_max = float(data['ref_max'])
            self.cat = data['cat']
        except KeyError as e:
            raise ValidationError("Invalid Metabolism: missing " + e.args[0])



class MetabolismSchema(ma.ModelSchema):
    refs = ma.Nested(RefSchema, many=True)
    class Meta:
        model=Metabolism