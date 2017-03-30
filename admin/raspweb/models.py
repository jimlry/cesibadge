from raspweb import app
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(autocommit = True, cursorclass=DictCursor)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)
cursor = mysql.connect().cursor()

class AdminModel:

	def getAdminByLoginAndPassword(self, login, password):
		cursor.execute("SELECT * FROM admin WHERE login = '" + login + "' AND password = '" + password +  "'")
		admin = cursor.fetchone()
		return admin

class BadgerModel:

	def getBadgerList(self):
		cursor.execute("SELECT * FROM badger")
		badgerlist = cursor.fetchall()
		return badgerlist

	def getBadgerListByBody(self, bodyId):
		cursor.execute("SELECT * FROM badger WHERE body_id = '" + bodyId + "'")
		badgerlist = cursor.fetchall()
		return badgerlist

	def getBadgerIdFromQrId(self, qrId):
		cursor.execute('Select id from badger WHERE badger.qr_id = "' + qrId + '"')
		badgerId = cursor.fetchone()
		return badgerId


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

	def getPresenceListByDate(self, date, roomId):
		cursor.execute("SELECT * FROM presence WHERE room_id = '" + roomId + "'AND (CAST(morning_date AS DATE) = '" + date + "' OR CAST(afternoon_date AS DATE) = '" + date + "')")
		presenceList = cursor.fetchall()
		return presenceList

	def getPresenceByBadgerId(self, badgerId):
		cursor.execute("SELECT * FROM presence WHERE badger_id = '" + str(badgerId) + "'")
		presence = cursor.fetchone()
		return presence

	def postPresence(self, badgerId, roomId, date):
		cursor.execute('INSERT INTO presence (badger_id, room_id, '+date+') VALUES("' + str(badgerId) + '" ,"' + str(roomId) + '", now())')

class BodyModel:

	def getBodyList(self):
		cursor.execute("SELECT * FROM body")
		bodyList = cursor.fetchall()
		return bodyList