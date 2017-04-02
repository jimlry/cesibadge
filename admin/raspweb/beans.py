class BadgerBean:
    def __init__(self, id, firstname, lastname, qrId, bodyName):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.qrId = qrId
        self.bodyName = bodyName

    id = 0;
    firstname = "";
    lastname = "";
    qrId = 0;
    bodyName = "";


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
    def __init__(self, badgerId, roomId, morningDate, afternoonDate):
        self.badgerId = badgerId
        self.roomId = roomId
        self.morningDate = morningDate
        self.afternoonDate = afternoonDate

    badgerId = 0
    roomId = 0
    morningDate = ""
    afterNoonDate = ""
