from ..extensions import db
from uuid import uuid4
import datetime
import json
from app.extensions import db, ma
from . import CRUD, ResultSchema
from app.exceptions import ValidationError


class Client(db.Model, CRUD):
    __tablename__ = 'clients'

    id = db.Column(db.String(45), primary_key=True)
    # 必需参数
    source_id = db.Column(db.String(45), db.ForeignKey('sources.id'))
    name = db.Column(db.String(255))
    gender = db.Column(db.SmallInteger())
    age = db.Column(db.SmallInteger())
    info = db.Column(db.JSON(), nullable=True)
    results = db.relationship(
        'Result',
        backref="client",
        lazy="dynamic"
    )
    # original_id = db.Column(db.String(45))
    # phone_num = db.Column(db.String(45), nullable=True)
    # height = db.Column(db.Float(), nullable=True)
    # weight = db.Column(db.Float(), nullable=True)
    # bmi = db.Column(db.Float(), nullable=True)

    # smoke = db.Column(db.Boolean(), default=False)
    # drink = db.Column(db.Boolean(), default=False)
    # triglyceride = db.Column(db.Float(), nullable=True)
    # cholesterol = db.Column(db.Float(), nullable=True)
    # h_lipoprotein = db.Column(db.Float(), nullable=True)
    # l_lipoprotein = db.Column(db.Float(), nullable=True)
    # fbg = db.Column(db.Float(), nullable=True)
    # defecate = db.Column(db.SmallInteger(), nullable=True)
    # medical_history = db.Column(db.Text(), nullable=True)
    # family_history = db.Column(db.Text(), nullable=True)
    # medicine = db.Column(db.Text(), nullable=True)
    # remarks = db.Column(db.Text(), nullable=True)


    # define relationship with result
    # results = db.relationship(
    #     'Result',
    #     backref='client',
    #     lazy='dynamic'
    # )

    def __init__(self):
        self.id = str(uuid4())


    def __repr__(self):
        return "<Model Client `{}`>".format(self.name)

    def import_data(self, data):
        try:
            self.name = data['name']
            self.source_id = data['source_id']
            self.gender = int(data['gender'])
            self.age = int(data['age'])
            self.info = data['info']
        except KeyError as e:
            raise ValidationError("Invalid Information: missing " + e.args[0])


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client
        include_fk=True
    results = ma.Nested(ResultSchema, many=True)