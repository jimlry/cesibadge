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

class BadgerModel:

	def getBadgerList(self):
		cursor.execute("SELECT * FROM badger")
		badgerlist = cursor.fetchall()
		return badgerlist

	def getBadgerListByBody(self, bodyId):
		cursor.execute("SELECT * FROM badger WHERE body_id = '" + bodyId + "'")
		badgerlist = cursor.fetchall()
		return badgerlist


class RoomModel:

	def getRoomList(self):
		cursor.execute("SELECT * FROM room")
		roomlist = cursor.fetchall()
		return roomlist

	def getRoomById(self, roomId):
		cursor.execute("SELECT * FROM room WHERE id = '" + roomId + "'")
		room = cursor.fetchone()
		return room


class PresenceModel:

	def getPresenceList(self):
		cursor.execute("SELECT * FROM presence")
		presenceList = cursor.fetchall()
		return presenceList

	def getPresenceListByDate(self, date):
		cursor.execute("SELECT * FROM presence WHERE CAST(morning_date AS DATE) = '" + date + "' OR CAST(afternoon_date AS DATE) = '" + date + "'")
		presenceList = cursor.fetchall()
		return presenceList


class BodyModel:

	def getBodyList(self):
		cursor.execute("SELECT * FROM body")
		bodyList = cursor.fetchall()
		return bodyList