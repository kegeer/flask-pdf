# from .. import

from ..extensions import db, ma
from . import CRUD
from app.exceptions import ValidationError

class Result(db.Model, CRUD):
    __tablename__ = 'results'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    client_id = db.Column(db.String(45), db.ForeignKey('clients.id'))
    original_id = db.Column(db.String(45))
    puyuan_id = db.Column(db.String(45), index=True)
    is_reported = db.Column(db.Boolean(), default=False)
    product_type= db.Column(db.SmallInteger())

    sampling_date = db.Column(db.DateTime(), nullable=True)
    receive_date = db.Column(db.DateTime(), nullable=True)
    test_date = db.Column(db.DateTime(), nullable=True)
    db.Column(db.TIMESTAMP,
              server_default=db.func.current_timestamp(), nullable=True)
    tester = db.Column(db.SmallInteger())
    auditor = db.Column(db.SmallInteger())

    content = db.Column(db.JSON())
    # client = db.relationship('Client', back_populates="results", lazy="dynamic")

    def __repr__(self):
        return "<Model Result `{}`>".format(self.client_id)

    def import_data(self, data):
        try:
            self.client_id = data['client_id']
            self.original_id = data['original_id']
            self.puyuan_id = data['puyuan_id']
            self.is_reported = data['is_reported']
            self.product_type = data['product_type']
            self.sampling_date = data['sampling_date']
            self.receive_date = data['receive_date']
            self.test_date = data['test_date']
            self.tester = data['tester']
            self.auditor = data['auditor']
            self.content = data['content']
        except KeyError as e:
            raise ValidationError("Invalid Information: missing " + e.args[0])


class ResultSchema(ma.ModelSchema):
    class Meta:
        model=Result
        include_fk=True
