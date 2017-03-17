from . import Info, RefSchema
from app.extensions import db, ma
from app.exceptions import ValidationError

class Disease(Info):

    __tablename__ = 'disease'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'di'
    }

    def __repr__(self):
        return "<Model Disease `{}`>".format(self.cat)

    def import_data(self, data):
        try:
            self.c_name = data['c_name']
            self.e_name = data['e_name']
            self.type = data['type']
            self.desc = data['desc']
            self.ref_min = float(data['ref_min'])
            self.ref_max = float(data['ref_max'])
        except KeyError as e:
            raise ValidationError("Invalid Disease: missing " + e.args[0])

class DiseaseSchema(ma.ModelSchema):
    refs = ma.Nested(RefSchema, many=True)
    class Meta:
        model = Disease