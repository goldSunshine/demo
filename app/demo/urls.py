from flask import Blueprint
from peewee import DoesNotExist

from app.demo import views

bp = Blueprint("demo", __name__)


@bp.errorhandler(DoesNotExist)
def handle_not_exist(error):
    return "no record", 404


bp.add_url_rule(
    "/demo/<int:demo_id>",
    view_func=views.Demo.as_view("demo"),
    methods=["GET", "POST", "PUT", "DELETE"],
)
bp.add_url_rule("/demos", view_func=views.Demos.as_view("demos"), methods=["GET"])
