from ..extensions import db
from uuid import uuid4
import datetime

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.String(45), primary_key=True)
    source = db.Column(db.SmallInteger())
    name = db.Column(db.String(255))
    phone_num = db.Column(db.String(45), nullable=True)
    original_id = db.Column(db.String(45))
    gender = db.Column(db.SmallInteger())
    age = db.Column(db.SmallInteger())
    height = db.Column(db.Float(), nullable=True)
    weight = db.Column(db.Float(), nullable=True)
    bmi = db.Column(db.Float(), nullable=True)
    inspector = db.Column(db.SmallInteger())
    auditor = db.Column(db.SmallInteger())
    smoke = db.Column(db.Boolean(), default=False)
    drink = db.Column(db.Boolean(), default=False)
    sampling_date = db.Column(db.DateTime(), nullable=True)
    receive_date = db.Column(db.DateTime(), nullable=True)
    inspect_date = db.Column(db.DateTime(), nullable=True)
    report_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    report = db.Column(db.Boolean(), default=False)
    triglyceride = db.Column(db.Float(), nullable=True)
    cholesterol = db.Column(db.Float(), nullable=True)
    h_lipoprotein = db.Column(db.Float(), nullable=True)
    l_lipoprotein = db.Column(db.Float(), nullable=True)
    fbg = db.Column(db.Float(), nullable=True)
    defecate = db.Column(db.SmallInteger(), nullable=True)
    medical_history = db.Column(db.Text(), nullable=True)
    family_history = db.Column(db.Text(), nullable=True)
    medicine = db.Column(db.Text(), nullable=True)
    remarks = db.Column(db.Text(), nullable=True)

    # define relationship with result
    results = db.relationship(
        'Result',
        backref='client',
        lazy='dynamic'
    )

    def __init__(self, name, source, puyuan_id):
        self.id = str(uuid4())
        self.name = name
        self.source = source
        self.puyuan_id = puyuan_id

    def __repr__(self):
        return "<Model Client `{}`>".format(self.name)
