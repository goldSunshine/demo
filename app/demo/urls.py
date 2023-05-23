from flask import Blueprint
from peewee import DoesNotExist
from app.demo import views

bp = Blueprint("demo", __name__)


@bp.errorhandler(DoesNotExist)
def handle_not_exist(error):
    return "not found"


bp.add_url_rule("/demo", view_func=views.Demo.as_view("demo"), methods=["GET", "PUT", "POST", "DELETE"])


