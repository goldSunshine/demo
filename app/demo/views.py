from flasgger import swag_from
from flask import jsonify, request
from flask.views import MethodView

from app.demo.models import DemoTable


class Demo(MethodView):
    @swag_from("./apidocs/get.yml")
    def get(self):
        query = request.values
        limit = int(query.get("limit", 10))
        offset = int(query.get("offset", 0))
        total, demos = DemoTable.get_with_page(limit, offset)
        return jsonify({"total": total, "result": demos})

    @swag_from("./apidocs/post.yml")
    def post(self):
        body = request.json
        DemoTable.create(**body)
        return jsonify({"res": "hello world"})


class DemoDetail(MethodView):
    @swag_from("./apidocs/put.yml")
    def put(self, demo_id):
        print(demo_id)
        body = request.json
        if not body:
            return "no value update", 400
        DemoTable.update_by_id(demo_id, body)
        return "success"

    @swag_from("./apidocs/delete.yml")
    def delete(self, demo_id):
        DemoTable.delete_by_id(demo_id)
        return jsonify({"msg": "success"})
