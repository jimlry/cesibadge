from raspweb import app
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from beans import BadgerBean

mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'raspberry'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)
cursor = mysql.connect().cursor()


class AdminModel:
    def getAdminByLoginAndPassword(self, login, password):
        cursor.execute("SELECT * FROM admin WHERE login = '" + login + "' AND password = '" + password + "'")
        admin = cursor.fetchone()
        return admin


class BadgerModel:
    def getBadgerBeanList(self):
        cursor.execute("SELECT * FROM badger")
        badgerList = cursor.fetchall()
        badgerBeanList = list()

        for badger in badgerList:
            badgerBean = BadgerBean(
                badger.get('id'),
                badger.get('firstname'),
                badger.get('lastname'),
                badger.get('qr_id'),
                badger.get('body_id')
            )
            badgerBeanList.append(badgerBean)

        return badgerBeanList

    def getBadgerList(self):
        cursor.execute("SELECT * FROM badger")
        badgerlist = cursor.fetchall()
        return badgerlist

    def getBadgerListByBody(self, bodyId):
        cursor.execute("SELECT * FROM badger WHERE body_id = '" + bodyId + "'")
        badgerlist = cursor.fetchall()
        return badgerlist

    def getBadgerIdFromQrId(self, qrId):
        cursor.execute('Select id from badger WHERE badger.qr_id = "' + qrId + '" ')
        badgerId = cursor.fetchone()
        return badgerId

    def postBadger(self, badger):
        print badger.bodyId
        query = (" \
          INSERT INTO badger (firstname, lastname, qr_id, body_id) \
          VALUES (%s, %s, %s, %s) \
        ")
        cursor.execute(query, (badger.firstname, badger.lastname, badger.qrId, badger.bodyId))


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
        cursor.execute(
            "SELECT * FROM presence WHERE room_id = '" + roomId + "'AND (CAST(morning_date AS DATE) = '" + date + "' OR CAST(afternoon_date AS DATE) = '" + date + "')")
        presenceList = cursor.fetchall()
        return presenceList

    def getPresenceByBadgerId(self, badgerId):
        cursor.execute("SELECT * FROM presence WHERE badger_id = '" + str(badgerId) + "'")
        presence = cursor.fetchall()
        return presence

    def postPresence(self, badgerId, roomId, date):
        cursor.execute = "INSERT INTO presence (badger_id, room_id, afternoon_date) VALUES (2, 1, now())"


class BodyModel:
    def getBodyList(self):
        cursor.execute("SELECT * FROM body")
        bodyList = cursor.fetchall()
        return bodyList