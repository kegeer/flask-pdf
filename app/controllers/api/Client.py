from app.models import Client, ClientSchema
from flask_restful import Resource
from flask import jsonify, request, make_response

schema = ClientSchema()

class ClientApi(Resource):
    def get(self, client_id=None):
        if client_id:
            client = Client.query.get(client_id)
            if client:
                return schema.dump(client).data
            else:
                return {'error': 'Info cannot be found'}
        # return schema.dump(Client.query.all()).data
        clients = Client.query.all()
        return schema.dump(clients, many=True).data
    def post(self):
        json = request.get_json()
        # return json
        if not json:
            return {'success': False, 'msg': 'NO Client provided'}, 400
        client = Client()
        client.import_data(json)
        client.add(client)
        return schema.dump(client).data

    def put(self, client_id):
        json = request.get_json(force=True)
        # return json
        client = Client.query.get_or_404(client_id)
        for key, value in json.items():
            setattr(client, key, value)
        client.update()
        return self.get(client_id)

    def delete(self, client_id):
        client = Client.query.get_or_404(client_id)
        client.delete(client)
        response = make_response()
        response.status_code = 204
        return response
