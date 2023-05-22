import peewee as pw
from app.db.base_model import BaseModel
from enum import IntEnum, unique


class DemoTable(BaseModel):
    @unique
    class Status(IntEnum):
        RUNNING = 0
        FINISHED = 1
        FAILURE = 2

    name = pw.CharField(max_length=128, default="")
    age = pw.IntegerField(index=True)
    user_id = pw.BigIntegerField()
    desc = pw.TextField()
    status = pw.SmallIntegerField(default=Status.RUNNING)
    sex = pw.BooleanField(default=0)

    class Meta:
        table_name = 'demo_table'


