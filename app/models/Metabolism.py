from . import Info
from ..extensions import db

class Metabolism(Info):

    __tablename__ = 'metabolism'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    cat = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'me'
    }

    def __repr__(self):
        return "<Model Metabolism `{}`>".format(self.cat)
