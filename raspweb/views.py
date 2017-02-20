from raspweb import app

from flask import render_template, request
import datetime
import calendar

@app.route('/')
def main():
	
	return render_template('index.html')	

@app.route('/badgerlist')
def badgerlist():
	badger = Badger()
	badgerlist = badger.getBadgerList()
	return render_template('userlist.html', badgerlist=badgerlist)	

@app.route('/roomlist')
def roomlist():
	cursor.execute("SELECT * FROM room")
	roomlist = cursor.fetchall()

	return render_template('roomlist.html', roomlist=roomlist)	

@app.route('/roomplanning', methods=['GET'])
def roomplanning():
	roomid = request.args.get('id')
	cursor.execute("SELECT * FROM room WHERE id='" + roomid + "'")
	room = cursor.fetchone();

	cursor.execute("SELECT * FROM presence")
	presenceList = cursor.fetchall()

	cursor.execute("SELECT * FROM badger")
	badgerList = cursor.fetchall()

	print calendar.TextCalendar(calendar.SUNDAY)

	morningDate = presenceList[1]['morning_date']
	print morningDate.isoweekday()

	return render_template('roomplanning.html', 
		room=room,
		presenceList=presenceList, 
		badgerList=badgerList)	

if __name__ == '__main__':
	app.run()
