class BadgerBean:
    def __init__(self, id, firstname, lastname, qrId, bodyBean):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.qrId = qrId
        self.bodyBean = bodyBean

    id = 0
    firstname = ""
    lastname = ""
    qrId = 0
    bodyBean = None


class RoomBean:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    id = 0
    name = ""


class BodyBean:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    id = 0
    name = ""


class AdminBean:
    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password

    id = 0
    login = ""
    password = ""


class PresenceBean:
    def __init__(self, badgerBean, roomBean, morningDate, afternoonDate):
        self.badgerBean = badgerBean
        self.roomBean = roomBean
        self.morningDate = morningDate
        self.afternoonDate = afternoonDate

    badgerBean = None
    roomBean = None
    morningDate = ""
    afterNoonDate = ""


class PlanningBean:
    def __init__(self, date, bodyBean, roomBean):
        self.date = date
        self.bodyBean = bodyBean
        self.roomBean = roomBean

    date = ""
    bodyBean = None
    roomBean = None