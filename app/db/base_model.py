import datetime
from peewee import Model, MySQLDatabase
from peewee import AutoField, DateTimeField

db = MySQLDatabase("test", host="127.0.0.1", port=3306, user="root", passwd="123456")


class BaseModel(Model):
    id = AutoField()
    create_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
