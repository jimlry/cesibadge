# -*- coding: utf-8 -*-
from raspweb import app
from flask import render_template, request, session, url_for, redirect
from models import BadgerModel, RoomModel, PresenceModel, BodyModel, AdminModel
from beans import BadgerBean
import json
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
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/badgerlist', methods=['GET', 'POST'])
def badgerlist():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    badgerModel = BadgerModel()

    if request.method == 'POST':
        badgerBean = BadgerBean(
            0,
            request.form['firstname'],
            request.form['lastname'],
            request.form['qrId'],
            request.form['bodyId']
        )
        badgerModel.postBadger(badgerBean)

    badgerBeanList = badgerModel.getBadgerBeanList()
    badgerList = badgerModel.getBadgerList()
    return render_template('userlist.html', badgerList=badgerList, badgerBeanList=badgerBeanList)


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


#Api de verification de l'existence de l'utilisateur en base
#Si existe: Renvoie id utilisateur
#Si existe pas: Renvoie "false"
@app.route('/verify_user', methods=['GET'])
def verify_user():
    # Récupération de l'id du qr_code
    request_param = request.form["id"]
    qrId = request_param.split("=")[1]
    # Requete SQL
    badgerModel = BadgerModel()
    badgerId = badgerModel.getBadgerIdFromQrId(qrId)
    if badgerId:
        return json.dumps(badgerId)
    else:
        return json.dumps(False)


#Met a jour la table presence de l'utilisateur
@app.route('/update_presence', methods=['POST'])
def update_presence():
    #Récupération de l'id de l'utilisateur a updater
    print 'REQUEST'

    jsonBadgerId = json.loads(request.form["id"])
    badgerId = jsonBadgerId["id"]

    roomId = request.form["room"]
    fieldToUpdate = get_field_to_update()

    #Requete SQL- Varie en fonction de si on est le matin ou l'aprem, et si l'utilisateur
    #est dans la table présence ou non
    presenceModel = PresenceModel()
    result = presenceModel.getPresenceByBadgerId(badgerId)

    print 'insert'
    presenceModel = PresenceModel()
    presenceModel.postPresence(badgerId, roomId, fieldToUpdate)

    # Return les résultats
    return json.dumps(True)

#Permet de savoir si l'utilisateur badge le matin ou l'aprem
def get_field_to_update():
    #Récupération de l'heure actuelle
    now = datetime.datetime.now()

    #On détermine si on est le matin ou l'après midi
    if now.hour < 12:
        field_to_update = "morning_date"
    else:
        field_to_update = "afternoon_date"
    return field_to_update

