from flask import Flask
from . import config

from .controllers.api import InfosApi
from .extensions import db, ma, api

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    ma.init_app(app)

    api.add_resource(
        InfosApi,
        '/api/infos',
        '/api/infos/<int:info_id>',
        endpoint='api_post'
    )
    api.init_app(app)

    return app