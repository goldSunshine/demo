from flask import request, jsonify
from flask.views import MethodView
from flasgger import swag_from
from app.demo.models import DemoTable


class Demo(MethodView):
    @swag_from('./apidocs/get.yml')
    def get(self):
        query = request.values
        limit = int(query.get("limit", 10))
        offset = int(query.get("offset", 0))
        total, demos = DemoTable.get_with_page(limit, offset)
        return jsonify({"total": total, "result": demos})

    @swag_from('./apidocs/post.yml')
    def post(self):
        body = request.json
        DemoTable.create(**body)
        return jsonify({"res": "hello world"})

    def put(self):
        pass

    def delete(self):
        pass