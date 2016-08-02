from flask import url_for, jsonify
from . import eqa
from .. import db

@eqa.route('/schemes/api/0.1/<int:item_id>')
@eqa.route('/schemes/api/0.1/')
def list_schemes(scheme_id=None):
    return jsonify({'sname': 'EQAI'})
