from beans import BadgerBean, RoomBean, BodyBean, AdminBean, PresenceBean
from raspweb import cursor

class AdminModel:
    def getAdminBeanByLoginAndPassword(self, login, password):
        query = "SELECT * FROM admin WHERE login = (%s) AND password = (%s)"
        cursor.execute(query, (login, password))
        admin = cursor.fetchone()

        adminBean = AdminBean(
            admin.get('id'),
            admin.get('login'),
            admin.get('password')

        )

        return adminBean


class BadgerModel:
    def getBadgerBeanList(self):
        cursor.execute("SELECT * FROM badger")
        badgerList = cursor.fetchall()
        badgerBeanList = list()
        bodyModel = BodyModel()

        for badger in badgerList:
            badgerBean = BadgerBean(
                badger.get('id'),
                badger.get('firstname'),
                badger.get('lastname'),
                badger.get('qr_id'),
                bodyModel.getBodyNameById(badger.get('body_id'))
            )
            badgerBeanList.append(badgerBean)

        return badgerBeanList

    def getBadgerBeanListByBody(self, bodyId):
        cursor.execute("SELECT * FROM badger WHERE body_id = '" + bodyId + "'")
        badgerList = cursor.fetchall()
        badgerBeanList = list()
        bodyModel = BodyModel()

        for badger in badgerList:
            badgerBean = BadgerBean(
                badger.get('id'),
                badger.get('firstname'),
                badger.get('lastname'),
                badger.get('qr_id'),
                bodyModel.getBodyNameById(badger.get('body_id'))
            )
            badgerBeanList.append(badgerBean)

        return badgerBeanList

    def getBadgerIdFromQrId(self, qrId):
        cursor.execute('SELECT id FROM badger WHERE badger.qr_id = "' + qrId + '" ')
        badgerId = cursor.fetchone()
        return badgerId

    def getBadgerListByQrId(self, qrId):
        cursor.execute('SELECT * FROM badger WHERE badger.qr_id = "' + qrId + '" ')
        badgerList = cursor.fetchall()
        badgerBeanList = list()
        bodyModel = BodyModel()

        for badger in badgerList:
            badgerBean = BadgerBean(
                badger.get('id'),
                badger.get('firstname'),
                badger.get('lastname'),
                badger.get('qr_id'),
                bodyModel.getBodyNameById(badger.get('body_id'))
            )
            badgerBeanList.append(badgerBean)

        return badgerBeanList

    def postBadger(self, badger):
        query = (
            "INSERT INTO badger (firstname, lastname, qr_id, body_id)"
            "VALUES (%s, %s, %s, %s)"
        )
        data = (badger.firstname, badger.lastname, badger.qrId, badger.bodyName)
        cursor.execute(query, data)


class RoomModel:
    def getRoomBeanList(self):
        cursor.execute("SELECT * FROM room")
        roomList = cursor.fetchall()
        roomBeanList = list()

        for room in roomList:
            roomBean = RoomBean(
                room.get('id'),
                room.get('name'),
            )
            roomBeanList.append(roomBean)

        return roomBeanList

    def getRoomBeanById(self, roomId):
        query = "SELECT * FROM room WHERE id = (%s)"
        cursor.execute(query, (roomId))
        room = cursor.fetchone()
        roomBean = RoomBean(
            room.get('id'),
            room.get('name')
        )

        return roomBean


class PresenceModel:
    def getPresenceBeanList(self):
        cursor.execute("SELECT * FROM presence")
        presenceList = cursor.fetchall()
        presenceBeanList = list()

        for presence in presenceList:
            presenceBean = PresenceBean(
                presence.get('badger_id'),
                presence.get('room_id'),
                presence.get('morning_date'),
                presence.get('afternoon_date')
            )
            presenceBeanList.append(presenceBean)

        return presenceBeanList

    def getPresenceBeanListByDate(self, date, roomId):
        cursor.execute(
            "SELECT * FROM presence WHERE room_id = '" + roomId + "'AND (CAST(morning_date AS DATE) = '" + date + "' OR CAST(afternoon_date AS DATE) = '" + date + "')")
        presenceList = cursor.fetchall()
        presenceBeanList = list()

        for presence in presenceList:
            presenceBean = PresenceBean(
                presence.get('badger_id'),
                presence.get('room_id'),
                presence.get('morning_date'),
                presence.get('afternoon_date')
            )
            presenceBeanList.append(presenceBean)

        return presenceList

    def getPresenceByBadgerId(self, badgerId):
        cursor.execute("SELECT * FROM presence WHERE badger_id = '" + str(badgerId) + "'")
        presence = cursor.fetchall()
        return presence

    def postPresence(self, badgerId, roomId, date):
        cursor.execute(
            'INSERT INTO presence (badger_id, room_id, ' + date + ') VALUES("' + str(badgerId) + '" ,"' + str(
                roomId) + '", now())')


class BodyModel:
    def getBodyBeanList(self):
        cursor.execute("SELECT * FROM body")
        bodyList = cursor.fetchall()
        bodyBeanList = list()

        for body in bodyList:
            bodyBean = BodyBean(
                body.get('id'),
                body.get('name')
            )
            bodyBeanList.append(bodyBean)

        return bodyBeanList

    def getBodyNameById(self, bodyId):
        query = ("SELECT body.name FROM body WHERE id = (%s)")
        cursor.execute(query, (bodyId))
        bodyName = cursor.fetchone().get('name')
        return bodyName