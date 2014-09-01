#peewee 
import datetime
from peewee import *

class Note(db.Model):
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)
