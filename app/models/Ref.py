from ..extensions import db, ma
from app.exceptions import ValidationError
from . import CRUD
class Ref(db.Model, CRUD):

    __tablename__ = 'refs'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    info_id = db.Column(db.Integer, db.ForeignKey('infos.id'))
    status = db.Column(db.SmallInteger())
    color = db.Column(db.SmallInteger())
    img = db.Column(db.SmallInteger())
    desc = db.Column(db.Text())

    def __repr__(self):
        return "<Model Ref `{}`>".format(self.info_id)

    def import_data(self, data):
        try:
            if 'info_id' in data:
                self.info_id = data['info_id']
            self.status = data['status']
            self.color = data['color']
            self.img = data['img']
            self.desc = data['desc']
        except ValueError as e:
            raise ValidationError("Invalid References: missing " + e.args[0])


class RefSchema(ma.ModelSchema):
    class Meta:
        model = Ref