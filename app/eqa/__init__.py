from flask import Blueprint

eqa = Blueprint('eqa', __name__)

from . import views
