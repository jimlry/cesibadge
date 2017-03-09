from raspweb import app
from flask import render_template, request, session, url_for, redirect
from models import BadgerModel, RoomModel, PresenceModel, BodyModel, AdminModel
import datetime, calendar, os

app.secret_key = os.urandom(24)

@app.route('/')
def main():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    adminModel = AdminModel()

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        admin = adminModel.getAdminByLoginAndPassword(login, password)
    
        if admin is None:
            error = "Identifiant ou Mot de passe invalide"
        else:
            session['logged_in'] = True
            session['admin'] = admin['login']
            return redirect(url_for('index'))

        error = 'Identifiant Invalide'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))


@app.route('/badgerlist')
def badgerlist():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    badgerModel = BadgerModel()
    badgerList = badgerModel.getBadgerList()
    return render_template('userlist.html', badgerList=badgerList)


@app.route('/roomlist')
def roomlist():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    roomModel = RoomModel()
    roomList = roomModel.getRoomList()
    return render_template('roomlist.html', roomList=roomList)


@app.route('/roomplanning', methods=['GET'])
def roomplanning():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    roomModel = RoomModel()
    presenceModel = PresenceModel()
    badgerModel = BadgerModel()
    bodyModel = BodyModel()
    presenceList = None
    datePicked = str(datetime.date.today())
    body = '1'

    roomId = request.args.get('id')
    if request.args.get('date'):
        datePicked = request.args.get('date')
    if request.args.get('body'):
        body = request.args.get('body')

    room = roomModel.getRoomById(roomId)
    presenceList = presenceModel.getPresenceListByDate(datePicked, roomId)
    badgerList = badgerModel.getBadgerListByBody(body)
    bodyList = bodyModel.getBodyList()

    return render_template('roomplanning.html',
                           room=room,
                           presenceList=presenceList,
                           badgerList=badgerList,
                           bodyList=bodyList,
                           datePicked=datePicked)