from application import db
# from application.models import alc_drink
# from application.models import soft_drink
# from application.models import prices
from application.models import Drinks


db.drop_all()
db.create_all()
