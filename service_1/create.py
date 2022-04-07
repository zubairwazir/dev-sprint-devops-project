from application import db
from application.models import Drinks


db.drop_all()
db.create_all()
