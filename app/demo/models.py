import peewee as pw
from app.db.base_model import BaseModel
from playhouse.shortcuts import model_to_dict
from enum import IntEnum, unique


class DemoTable(BaseModel):

    @unique
    class Status(IntEnum):
        RUNNING = 0
        FINISHED = 1
        FAILURE = 2

    name = pw.CharField(max_length=128, default="")
    age = pw.IntegerField()
    user_id = pw.BigIntegerField(index=True)
    desc = pw.TextField()
    status = pw.SmallIntegerField(default=Status.RUNNING.value)
    sex = pw.BooleanField(default=0)

    class Meta:
        table_name = 'demo_table'

    @classmethod
    def get_with_page(cls, limit, offset):
        query = cls.select()
        total = query.count()
        res = query.order_by(cls.id).offset(offset).limit(limit)
        demos = [model_to_dict(i) for i in res]
        return total, demos

    @classmethod
    def delete_by_id(cls, demo_id):
        # 检查是否存在该demo_id，如果不存在则抛出异常404
        res = cls.get(cls.id==demo_id)
        res.delete_instance()

    @classmethod
    def update_by_id(cls, demo_id, args):
        # 检查是否存在该demo_id，如果不存在则抛出异常404
        res = cls.get(cls.id == demo_id)
        q = res.update(**args)
        q.execute()



