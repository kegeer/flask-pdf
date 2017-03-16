from . import Info
from ..extensions import db

class Disease(Info):

    __tablename__ = 'disease'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    # cat = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'di'
    }

    def __repr__(self):
        return "<Model Disease `{}`>".format(self.cat)