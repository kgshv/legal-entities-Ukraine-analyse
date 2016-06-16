from db_models import Uoutf, db
db.connect()




sanated = Uoutf.select().where(Uoutf.status == "порушено справу про банкрутство (санація)") # This is same as:
# SELECT * FROM uoutf
# WHERE status = "порушено справу про банкрутство (санація)";
# You can also loop through this object