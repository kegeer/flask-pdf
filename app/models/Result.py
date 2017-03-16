# from .. import db
from ..extensions import db
from uuid import uuid4

class Result(db.Model):
    __tablename__ = 'results'

    client_id = db.Column(db.String(45), db.ForeignKey('clients.id'))
    puyuan_id = db.Column(db.String(45), primary_key=True)
    content = db.Column(db.JSON())

    def __init__(self):
        self.id = str(uuid4())

    def __repr__(self):
        return "<Model Result `{}`>".format(self.client_id)
