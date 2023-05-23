from app.db import base_model
from app.db.base_model import db
from peewee_migrate import Router
from app.demo import models as demo_models

# 需要迁移的数据库表
migrate_tables = [demo_models]

db.connect()
router = Router(db, ignore='basemodel')
# router.create(auto=migrate_tables)
router.run()
db.close()



