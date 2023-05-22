from flask import Blueprint
from app.demo import api as v

bp = Blueprint("demo", __name__)

bp.add_url_rule("/demo", view_func=v.Demo.as_view("demo"),)