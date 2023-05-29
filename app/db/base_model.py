import datetime

from peewee import AutoField, DateTimeField, Model, MySQLDatabase
from playhouse.shortcuts import model_to_dict

db = MySQLDatabase("test", host="10.30.20.244", port=3306, user="root", passwd="123456")


class BaseModel(Model):
    id = AutoField()
    create_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def to_dict(self):
        exclude = set()
        for exclude_field_name in self.__exclude__:
            exclude.add(self._meta.combined[exclude_field_name])
        return model_to_dict(self, exclude=exclude)
