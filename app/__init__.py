from flask import Flask
from . import config

from .controllers.api import InfoApi, ClientApi, SourcesList, SourcesUpdate, ResultsList, ResultsUpdate, ReportApi
from .extensions import db, ma, api, cors

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # api.add_resource(InfosList, '/api/infos')
    # api.add_resource(InfosUpdate, '/<int:id>.json')
    # api.add_resource(
    #     InfosApi,
    #     '/api/infos',
    #     '/api/infos/<int:info_id>',
    #     endpoint='api_post'
    # )
    api.add_resource(InfoApi, '/api/infos', '/api/infos/<int:info_id>', endpoint='api_info')
    api.add_resource(ClientApi, '/api/clients', '/api/clients/<string:client_id>', endpoint='api_client')
    api.add_resource(SourcesUpdate, '/api/sources/<string:source_id>', endpoint='api_source')
    api.add_resource(SourcesList, '/api/sources', endpoint='api_sources')
    api.add_resource(ResultsList, '/api/results', endpoint='api_results')
    api.add_resource(ResultsUpdate, '/api/results/<string:result_id>', endpoint='api_result')
    api.add_resource(ReportApi, '/api/report', endpoint='api_report')
    api.init_app(app)

    return app