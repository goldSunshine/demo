from flasgger import swag_from
from flask import request
from flask.views import MethodView

from app.demo.models import DemoTable
from app.extensions import json_response


class Demo(MethodView):
    @swag_from("./apidocs/get.yml")
    def get(self):
        query = request.values
        limit = int(query.get("limit", 10))
        offset = int(query.get("offset", 0))
        total, demos = DemoTable.get_with_page(limit, offset)
        return json_response(data={"total": total, "result": demos})

    @swag_from("./apidocs/post.yml")
    def post(self):
        body = request.json
        res = DemoTable.create(**body)

        # 返回json格式的数据，数据必须可以json序列化
        # to_dict 方法可以将对象转成字典
        return json_response(data=res.to_dict())


class DemoDetail(MethodView):
    @swag_from("./apidocs/put.yml")
    def put(self, demo_id):
        body = request.json
        if not body:
            return json_response(code=400, data={"msg": "没有传入更新的数据"})
        DemoTable.update_by_id(demo_id, body)
        return json_response(code=200)

    @swag_from("./apidocs/delete.yml")
    def delete(self, demo_id):
        DemoTable.delete_by_id(demo_id)

        # 接口返回值可以只有状态码，200表示操作成功 404表示找不到对象 400表示错误
        return json_response(code=200)
