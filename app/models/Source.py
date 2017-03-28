from app.extensions import db, ma
from uuid import uuid4
from . import CRUD, ClientSchema
from app.exceptions import ValidationError

class Source(db.Model, CRUD):

    __tablename__='sources'

    id=db.Column(db.String(45), primary_key=True)
    name=db.Column(db.String(10), nullable=True)

    clients = db.relationship(
        'Client',
        backref='source',
        lazy='dynamic'
    )

    def __init__(self):
        self.id = str(uuid4())


    def __repr__(self):
        return "<Model Source `{}`>".format(self.name)

    def import_data(self, data):
        try:
            self.name = data['name']
        except KeyError as e:
            raise ValidationError("Invalid Information: missing " + e.args[0])

class SourceSchema(ma.ModelSchema):
    clients = ma.Nested(ClientSchema, many=True)
    class Meta:
        model = Source
