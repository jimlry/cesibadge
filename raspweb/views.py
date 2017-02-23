from raspweb import app
from flask import render_template, request
import datetime, calendar
from models import BadgerModel, RoomModel, PresenceModel

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

	roomId = request.args.get('id')
	room = roomModel.getRoomById(roomId)
	badgerList = badgerModel.getBadgerList()
	presenceList = presenceModel.getPresenceList()

	return render_template('roomplanning.html', 
		room=room,
		presenceList=presenceList, 
		badgerList=badgerList)