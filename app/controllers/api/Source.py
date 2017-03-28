from app.models import Source, SourceSchema
from flask_restful import Resource
from flask import request, jsonify, make_response
from app.extensions import db

from sqlalchemy.exc import SQLAlchemyError
schema = SourceSchema()

class SourcesList(Resource):
    def get(self):
        sources = schema.dump(Source.query.all(), many=True).data
        return sources
    def post(self):
        raw_json = request.get_json(force=True)
        # return raw_json
        try:
            source = Source()
            source.import_data(raw_json)
            source.add(source)
            query = Source.query.get(source.id)
            sources = schema.dump(query).data
            return sources, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

class SourcesUpdate(Resource):
    def get(self, source_id):
        source = schema.dump(self.getSource(source_id)).data
        return source
    def patch(self, source_id):
        source = self.getSource(source_id)
        raw_json = request.get_json(force=True)
        try:
            for key, value in raw_json.items():
                setattr(source, key, value)
            source.update()
            return self.get(source_id)
        except SQLAlchemyError as e:
            self.respSqlError(e)
    def delete(self, source_id):
        source = self.getSource(source_id)
        try:
            delete = source.delete(source)
            resp = make_response()
            resp.status_code=204
            return resp
        except SQLAlchemyError as e:
            self.respSqlError(e)

    def getSource(self, source_id):
        return Source.query.get_or_404(source_id)
    def respSqlError(self, e):
        db.session.rollback()
        resp = jsonify({"error": str(e)})
        resp.status_code = 401
        return resp



