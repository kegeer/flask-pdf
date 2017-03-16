from . import Info
from ..extensions import db

class Species(Info):

    __tablename__ = 'species'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    cat = db.Column(db.String(10))

    __mapper_args__ = {
        'polymorphic_identity': 'sp'
    }

    def __repr__(self):
        return "<Model Species `{}`>".format(self.cat)
