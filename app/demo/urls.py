from flask import Blueprint
from peewee import DoesNotExist
from app.demo import views

bp = Blueprint("demo", __name__)


@bp.errorhandler(DoesNotExist)
def handle_not_exist(error):
    return "no record", 404


bp.add_url_rule("/demo/<int:demo_id>", view_func=views.DemoDetail.as_view("demo_detail"), methods=["PUT", "DELETE"])
bp.add_url_rule("/demo", view_func=views.Demo.as_view("demo"), methods=["GET", "POST"])



