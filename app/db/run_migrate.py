from app.db.base_model import db, BaseModel
from peewee_migrate import Router

from app.demo.models import DemoTable


db.connect()

router = Router(db, ignore='basemodel')
router.create(auto=BaseModel)

router.run()
db.close()



