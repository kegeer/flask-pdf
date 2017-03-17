from app.extensions import db

class CRUD():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

from .Result import Result
from .Ref import Ref, RefSchema
from .Client import Client
from .Info import Info, InfoSchema
from .Disease import Disease, DiseaseSchema
from .General import General, GeneralSchema
from .Genus import Genus, GenusSchema
from .Metabolism import Metabolism, MetabolismSchema
from .Species import Species, SpeciesSchema