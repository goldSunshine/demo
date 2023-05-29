from enum import IntEnum, unique

import peewee as pw
from functools import cached_property

from app.db.base_model import BaseModel


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

    # 数据库对象转字典时需要移除的字段
    __exclude__ = ["desc", "sex"]

    class Meta:
        table_name = "demo_table"

    @classmethod
    def get_with_page(cls, limit, offset):
        query = cls.select()
        total = query.count()
        res = query.order_by(cls.id).offset(offset).limit(limit)
        demos = [i.to_dict() for i in res]
        return total, demos

    @classmethod
    def delete_by_id(cls, demo_id):
        # 检查是否存在该demo_id，如果不存在则抛出异常404
        res = cls.get(cls.id == demo_id)
        res.delete_instance()

    @classmethod
    def update_by_id(cls, demo_id, args):
        # 检查是否存在该demo_id，如果不存在则抛出异常404
        res = cls.get(cls.id == demo_id)
        q = res.update(**args)
        q.execute()

    @classmethod
    def get_by_demo_id(cls, demo_id):
        res = cls.get(cls.id == demo_id)
        return res
