from os import path
import pdfkit
from app.models import Result, ResultSchema
from flask_restful import Resource
from flask import request, make_response, render_template
from app.extensions import db
from jinja2 import Template, Environment, FileSystemLoader

from sqlalchemy.exc import SQLAlchemyError
schema = ResultSchema()
# THIS_DIR = path.dirname(path.abspath())
TEMPLATE_DIR=path.abspath(path.join(path.dirname(__file__), path.pardir, path.pardir, 'pdfs', 'mendel'))
class ReportApi(Resource):
    def post(self):
        json = request.get_json(force=True)
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
        tmpl = env.get_template('mendel.html')
        css = path.join(path.dirname(__file__), '../../pdfs/mendel/mendel.css')
        page = render_template(tmpl,
                               client=json['client'],
                               result=json['result'],
                               general=json['general'],
                               meta3=json['meta3'],
                               vitamin=json['vitamin'],
                               patho=json['patho']
                               )
        pdf = pdfkit.from_string(page, False, css=css)
        resp =make_response(pdf)
        resp.headers['Content-Type'] = 'application/pdf'
        resp.headers['Content-Disposition'] = 'attachment; filename=mendel.pdf'
        return resp

