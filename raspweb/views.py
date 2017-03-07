from raspweb import app
from flask import render_template, request
import datetime, calendar
from models import BadgerModel, RoomModel, PresenceModel, BodyModel

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/badgerlist')
def badgerlist():
    badgerModel = BadgerModel()
    badgerList = badgerModel.getBadgerList()
    return render_template('userlist.html', badgerList=badgerList)


@app.route('/roomlist')
def roomlist():
    roomModel = RoomModel()
    roomList = roomModel.getRoomList()
    return render_template('roomlist.html', roomList=roomList)


@app.route('/roomplanning', methods=['GET'])
def roomplanning():
    roomModel = RoomModel()
    presenceModel = PresenceModel()
    badgerModel = BadgerModel()
    bodyModel = BodyModel()
    presenceList = None
    datePicked = str(datetime.date.today())

    print datePicked

    roomId = request.args.get('id')

    if request.args.get('date'):
        datePicked = request.args.get('date')
    
    if request.args.get('date'):
        body = request.args.get('body')

    presenceList = presenceModel.getPresenceListByDate(datePicked)
    room = roomModel.getRoomById(roomId)

    badgerList = badgerModel.getBadgerListByBody(body)
    bodyList = bodyModel.getBodyList()

    return render_template('roomplanning.html',
                           room=room,
                           presenceList=presenceList,
                           badgerList=badgerList,
                           bodyList=bodyList,
                           datePicked=datePicked)
