from ..extensions import db, ma

class Ref(db.Model):

    __tablename__ = 'refs'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    info_id = db.Column(db.Integer, db.ForeignKey('infos.id'))
    status = db.Column(db.SmallInteger())
    color = db.Column(db.SmallInteger())
    img = db.Column(db.SmallInteger())
    desc = db.Column(db.Text())

    def __repr__(self):
        return "<Model Ref `{}`>".format(self.info_id)

class RefSchema(ma.ModelSchema):
    class Meta:
        model = Ref