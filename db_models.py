from peewee import *

db = SqliteDatabase('payers.db')

class Uoutf(Model):
	name = CharField()
	short_name = CharField()
	taxpayer_code = IntegerField(null=True)
	address = CharField()
	director_name = CharField()
	major_activity = CharField()
	status = CharField()

	class Meta:
		database = db # This model uses the "payers.db" database.