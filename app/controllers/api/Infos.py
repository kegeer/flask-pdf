from app.models import Info, InfoSchema
from flask_restful import Resource
from flask import request, jsonify, make_response
from app.extensions import db
schema = InfoSchema

from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError


class InfosList(Resource):
    def get(self):
        infos_query = Info.query.all()
        infos = schema.dump(infos_query, many=True).data
        return infos
    def post(self):
        raw_dict = request.get_json(force=True)
        info_dict = raw_dict['data']['attibutes']
        try:
            schema.validate(info_dict)
            info = Info(info_dict['c_name'], info_dict['e_name'])
            info.add(info)
            query = Info.query.get(info.id)
            results = schema.dump(query).data
            return results, 201
        except ValidationError as err:
            resp = jsonify({'error': err.messages})
            resp.status_code = 403
            return resp
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({'error': str(e)})
            resp.status_code = 403
            return resp

class InfosUpdate(Resource):
    def get(self, info_id=None):
        info_query = Info.query.get_or_404(info_id)
        info = schema.dump(info_query).data
        return info
    def patch(self, info_id):
        info = Info.query.get_or_404(info_id)
        raw_dict = request.get_json(force=True)
        info_dict = raw_dict['data']['attributes']
        try:
            for key, value in info_dict.items():
                schema.validate({key:value})
                setattr(info, key, value)
            info.update()
            return self.get(info_id)
        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp
    def delete(self, info_id):
        info = Info.query.get_or_404(info_id)
        try:
            delete = info.delete(info)
            response = make_response()
            response.status_code = 204
            return response
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({'error': str(e)})
            resp.status_code = 401
            return resp

