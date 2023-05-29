import datetime

from peewee import AutoField, DateTimeField, Model, MySQLDatabase
from playhouse.shortcuts import model_to_dict

from config import db_host, db_name, db_passwd, db_port, db_user

db = MySQLDatabase(
    database=db_name, host=db_host, port=db_port, user=db_user, passwd=db_passwd
)


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
