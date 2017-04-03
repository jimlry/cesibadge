from beans import BadgerBean, RoomBean, BodyBean, AdminBean, PresenceBean, PlanningBean
from raspweb import cursor

class AdminModel:
    def getAdminBeanByLoginAndPassword(self, login, password):
        query = (
            "SELECT * "
            "FROM admin "
            "WHERE login = (%s) "
            "AND password = (%s)"
        )
        cursor.execute(query, (login, password))
        admin = cursor.fetchone()
        adminBean = None
        if admin is None:
            return adminBean
        else :
            adminBean = AdminBean(
                admin.get('id'),
                admin.get('login'),
                admin.get('password')

            )
            return adminBean


class BadgerModel:
    def getBadgerBeanById(self, badgerId):
        query = (
            "SELECT * "
            "FROM badger "
            "WHERE id = (%s)")
        cursor.execute(query, (badgerId))
        badger = cursor.fetchone()
        bodyModel = BodyModel()

        badgerBean = BadgerBean(
            badger.get('id'),
            badger.get('firstname'),
            badger.get('lastname'),
            badger.get('qr_id'),
            bodyModel.getBodyBeanById(badger.get('body_id'))
        )

        return badgerBean

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
                bodyModel.getBodyBeanById(badger.get('body_id'))
            )
            badgerBeanList.append(badgerBean)

        return badgerBeanList

    def getBadgerBeanListByBodyId(self, bodyId):
        query = (
            "SELECT * "
            "FROM badger "
            "WHERE body_id = (%s) "
        )
        cursor.execute(query, (bodyId))
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
        query = (
            "SELECT id "
            "FROM badger "
            "WHERE badger.qr_id = (%s) "
        )
        cursor.execute(query, (qrId))
        badgerId = cursor.fetchone()
        return badgerId

    def getBadgerListByQrId(self, qrId):
        query = (
            "SELECT * "
            "FROM badger "
            "WHERE badger.qr_id = (%s) "
        )
        cursor.execute(query, (qrId))
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
        cursor.execute(query, (badger.firstname, badger.lastname, badger.qrId, badger.bodyName))


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
        badgerModel = BadgerModel()
        roomModel = RoomModel()

        for presence in presenceList:
            presenceBean = PresenceBean(
                badgerModel.getBadgerBeanById(presence.get('badger_id')),
                roomModel.getRoomBeanById(presence.get('room_id')),
                presence.get('morning_date'),
                presence.get('afternoon_date')
            )
            presenceBeanList.append(presenceBean)

        return presenceBeanList

    def getPresenceBeanListByDateAndRoomId(self, date, roomId):
        query = (
             "SELECT * "
             "FROM presence "
             "WHERE room_id = (%s) "
             "AND (CAST(morning_date AS DATE) = (%s) "
             "OR CAST(afternoon_date AS DATE) = (%s)) "
        )
        cursor.execute(query, (roomId, date, date))
        presenceList = cursor.fetchall()
        presenceBeanList = list()
        badgerModel = BadgerModel()
        roomModel = RoomModel()

        for presence in presenceList:
            presenceBean = PresenceBean(
                badgerModel.getBadgerBeanById(presence.get('badger_id')),
                roomModel.getRoomBeanById(presence.get('room_id')),
                presence.get('morning_date'),
                presence.get('afternoon_date')
            )
            presenceBeanList.append(presenceBean)

        return presenceBeanList

    def getPresenceByBadgerId(self, badgerId):
        query = (
            "SELECT * "
            "FROM presence "
            "WHERE badger_id = (%s) "
        )
        cursor.execute(query, (badgerId))
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
        query = (
            "SELECT body.name "
            "FROM body "
            "WHERE id = (%s)")
        cursor.execute(query, (bodyId))
        bodyName = cursor.fetchone().get('name')
        return bodyName

    def getBodyBeanById(self, bodyId):
        query = (
            "SELECT * "
            "FROM body "
            "WHERE id = (%s)")
        cursor.execute(query, (bodyId))
        body = cursor.fetchone()

        bodyBean = BodyBean(
            body.get('id'),
            body.get('name')
        )

        return bodyBean


class PlanningModel:
    def getPlanningBeanListByBodyIdAndRoomId(self, bodyId, roomId):
        query = (
            "SELECT * "
            "FROM planning "
            "WHERE body_id = (%s) "
            "AND  room_id = (%s) "
        )
        cursor.execute(query, (bodyId, roomId))
        planningList = cursor.fetchall()
        planningBeanList = list()
        bodyModel = BodyModel()
        roomModel = RoomModel()

        for planning in planningList:
            planningBean = PlanningBean(
                planning.get('date'),
                bodyModel.getBodyBeanById(planning.get('body_id')),
                roomModel.getRoomBeanById(planning.get('room_id'))
            )
            planningBeanList.append(planningBean)

        return planningBeanList

    def getPlanningBeanList(self):
        cursor.execute("SELECT * FROM planning")
        planningList = cursor.fetchall()
        planningBeanList = list()
        bodyModel = BodyModel()
        roomModel = RoomModel()

        for planning in planningList:
            planningBean = PlanningBean(
                planning.get('date'),
                bodyModel.getBodyBeanById(planning.get('body_id')),
                roomModel.getRoomBeanById(planning.get('room_id'))
            )
            planningBeanList.append(planningBean)

        return planningBeanList