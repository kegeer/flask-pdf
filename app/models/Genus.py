from . import Info
from ..extensions import db

class Genus(Info):

    __tablename__ = 'genus'

    id = db.Column(db.Integer, db.ForeignKey('infos.id'), primary_key=True)
    cat = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'ge'
    }

    def __repr__(self):
        return "<Model Genus `{}`>".format(self.cat)