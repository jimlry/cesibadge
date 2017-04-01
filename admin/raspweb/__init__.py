from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import os

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    MYSQL_DATABASE_USER = 'root',
    MYSQL_DATABASE_PASSWORD = 'root',
    MYSQL_DATABASE_DB = 'raspberry',
    MYSQL_DATABASE_HOST = '127.0.0.1',
    DEBUG = True,
    SECRET_KEY = os.urandom(24)
))

db = MySQL(cursorclass=DictCursor)
db.init_app(app)
cursor = db.connect().cursor()

from raspweb import views
