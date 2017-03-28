from app.models import Info, InfoSchema, Metabolism, MetabolismSchema, Ref, General, GeneralSchema, Genus, GenusSchema, Species, SpeciesSchema, Disease, DiseaseSchema
from flask_restful import Resource
from flask import jsonify, abort, request, make_response

# Define the serializer
InfoSer = InfoSchema()
MetaSer = MetabolismSchema()

class InfoApi(Resource):
    def get(self, info_id=None):

        if info_id:
            info = Info.query.get(info_id)
            if info:
                return InfoSer.dump(info).data
            else:
                return {'error': 'Info cannot be found'}

        return InfoSer.dump(Info.query.all(), many=True).data

    def post(self):
        json = request.get_json(force=True)
        if not json:
            return {'success': False, 'msg': 'NO Info provided'}, 400
        return self.entity_add(json)

    def put(self, info_id):
        json = request.get_json(force=True)
        # return json
        self.update_refs(json)
        type = json['type']
        self.entity_update(type, info_id, json)
        return self.get(info_id)

    def delete(self, info_id):
        info = Info.query.get_or_404(info_id)
        info.delete(info)
        response = make_response()
        response.status_code = 204
        return response

    def entity_add(self, json):
        en_type = json['type']
        if en_type == "":
            json['type'] = "info"
            entity = Info()
            schema = InfoSchema()
        else:
            if type == "me":
                entity = Metabolism()
                schema = MetabolismSchema()
            elif type == 'gn':
                entity = General()
                schema = GeneralSchema()
            elif type == 'ge':
                entity = Genus()
                schema = GenusSchema()
            elif type == 'sp':
                entity = Species()
                schema = SpeciesSchema()
            elif type == 'di':
                entity = Disease()
                schema = DiseaseSchema()
        entity.import_data(json)
        refs = json['refs']
        for ref in refs:
            new_ref = Ref()
            new_ref.import_data(ref)
            entity.refs.append(new_ref)
        entity.add(entity)
        return schema.dump(entity).data

    def entity_update(self, type, info_id, json):
        if type == 'info':
            entity = Info()
        elif type == 'gn':
            entity = General()
        elif type == 'me':
            entity = Metabolism()
        elif type == 'ge':
            entity = Genus()
        elif type == 'sp':
            entity = Species()
        elif type == 'di':
            entity = Disease()
        else:
            abort(401)

        val = entity.query.get_or_404(info_id)

        for key, value in json.items():
            setattr(val, key, value)
        val.update()

    def update_refs(self, json):
        refs = json.pop('refs')
        ref = Ref()
        for re in refs:
            if re['id'] and 'id' in re:
                ref_query = ref.query.get(re['id'])
                for key, value in re.items():
                    setattr(ref_query, key, value)
                    ref_query.update()
            else:
                re['info_id'] = json['id']
                ref.import_data(re)
                ref.add(ref)
