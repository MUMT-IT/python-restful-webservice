from flask import url_for, jsonify
from . import eqa
from .. import db

@eqa.route('/api/0.1/schemes/<int:item_id>')
@eqa.route('/api/0.1/schemes/')
def list_schemes(scheme_id=None):
    return jsonify({'sname': 'EQAI'})
