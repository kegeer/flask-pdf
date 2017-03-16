from app.models import Info, InfoSchema
from flask_restful import Resource
from flask import jsonify, abort, request
from app.extensions import db

# Define the serializer
InfoSer = InfoSchema()


class InfoApi(Resource):
    def get(self, info_id=None):

        if info_id:
            info = Info.query.get(info_id)
            if info:
                return InfoSer.dump(info)
            else:
                return {'error': 'Info cannot be found'}

        return InfoSer.dump(Info.query.all(), many=True).data

    def post(self, info_id=None):
        if info_id:
            abort(400)
        json = request.get_json()
        if not json:
            return {'success': False, 'msg': 'NO Info provided'}, 400

        result = InfoSer.load(json).data
        # db.session.add(result)
        # db.session.commit()
        return InfoSer.dump(result).data