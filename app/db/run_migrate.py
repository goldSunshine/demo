import sys
from peewee_migrate import Router

from app.db.base_model import db
from app.demo import models as demo_models

# 需要迁移的数据库表, 所有数据新增、修改的都需要引入
migrate_tables = [demo_models]


def create_migrate():
    db.connect()
    router = Router(db, ignore="basemodel")
    router.create(auto=migrate_tables)
    db.close()


def run_migrate():
    db.connect()
    router = Router(db, ignore="basemodel")
    router.run()
    db.close()


if __name__ == "__main__":
    action = sys.argv[1]
    if action == "run_migrate":
        run_migrate()
    elif action == "create_migrate":
        create_migrate()
