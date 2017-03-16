from . import Info
from ..extensions import db

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