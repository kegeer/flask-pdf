from app.models import Result, ResultSchema, Info, InfoSchema
from flask_restful import Resource
from flask import request, jsonify, make_response
from app.extensions import db

from sqlalchemy.exc import SQLAlchemyError
schema = ResultSchema()

class ResultsList(Resource):
    def get(self):
        results = schema.dump(Result.query.all(), many=True).data
        return results
    def post(self):
        raw_json = request.get_json(force=True)
        try:
            result = Result()
            result.import_data(raw_json)
            result.add(result)
            query = Result.query.get(result.id)
            results = schema.dump(query).data
            return results, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

class ResultsUpdate(Resource):
    def get(self, result_id):
        infoSchema = InfoSchema()
        infos = infoSchema.dump(Info.query.all()).data
        result = schema.dump(self.getResult(result_id)).data

        report = []
        if result['content']:
            for result in result['content']:
                id = int(result['id'])
                for info in infos:
                    if info['id'] == id:
                        info['value'] = result['value']
                        for ref in info['refs']:
                            if ref['status'] == int(result['status']):
                                info['color'] = ref['color']
                                info['img'] = ref['img']
                                info['summary'] = ref['desc']
                                info.pop('refs')
                                report.append(info)
                                break
        return result, report
    def patch(self, result_id):
        result = self.getResult(result_id)
        raw_json = request.get_json(force=True)
        try:
            for key, value in raw_json.items():
                setattr(result, key, value)
            result.update()
            return self.get(result_id)
        except SQLAlchemyError as e:
            self.respSqlError(e)
    def delete(self, result_id):
        result = self.getResult(result_id)
        try:
            delete = result.delete(result)
            resp = make_response()
            resp.status_code=204
            return resp
        except SQLAlchemyError as e:
            self.respSqlError(e)

    def getResult(self, result_id):
        return Result.query.get_or_404(result_id)
    def respSqlError(self, e):
        db.session.rollback()
        resp = jsonify({"error": str(e)})
        resp.status_code = 401
        return resp



