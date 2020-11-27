from flask import Blueprint


bp = Blueprint("index", __name__)

# necessary, must after bp = Blueprint("index", __name__)
from . import urls
