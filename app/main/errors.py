from flask import jsonify
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'page not found'})

@main.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'internal server error'})