from raspweb import app

from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'raspberry'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)
cursor = mysql.connect().cursor()

class Badger:

	def getBadgerList():
		cursor.execute("SELECT * FROM badger")
		badgerlist = cursor.fetchall()

		return badgerlist