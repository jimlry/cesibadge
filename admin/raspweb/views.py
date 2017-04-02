# -*- coding: utf-8 -*-
from raspweb import app
from flask import render_template, request, session, url_for, redirect
from models import BadgerModel, RoomModel, PresenceModel, BodyModel, AdminModel
from beans import BadgerBean
import json
import datetime


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
        adminBean = adminModel.getAdminBeanByLoginAndPassword(login, password)

        if adminBean is None:
            error = "Identifiant ou Mot de passe invalide"
        else:
            session['logged_in'] = True
            session['admin'] = adminBean.login
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

    error = None
    badgerModel = BadgerModel()

    if request.method == 'POST':
        if badgerModel.getBadgerListByQrId(request.form['qrId']) is None:
            error = "Ce QR ID est déjà utilisé"
        else:
            badgerBean = BadgerBean(
                0,
                request.form['firstname'],
                request.form['lastname'],
                request.form['qrId'],
                request.form['bodyName']
            )
            badgerModel.postBadger(badgerBean)

    badgerBeanList = badgerModel.getBadgerBeanList()
    return render_template(
        'badgerlist.html',
        badgerBeanList=badgerBeanList,
        error=error
    )


@app.route('/roomlist')
def roomlist():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    roomModel = RoomModel()
    roomBeanList = roomModel.getRoomBeanList()
    return render_template('roomlist.html', roomBeanList=roomBeanList)


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

    roomBean = roomModel.getRoomBeanById(roomId)
    presenceBeanList = presenceModel.getPresenceBeanListByDateAndRoomId(datePicked, roomId)
    badgerBeanList = badgerModel.getBadgerBeanListByBodyId(body)
    bodyBeanList = bodyModel.getBodyBeanList()

    return render_template(
        'roomplanning.html',
        room = roomBean,
        presenceBeanList = presenceBeanList,
        badgerBeanList = badgerBeanList,
        bodyBeanList = bodyBeanList,
        datePicked = datePicked
    )


@app.route('/verify_user', methods=['GET'])
def verify_user():
    request_param = request.form["id"]
    qrId = request_param.split("=")[1]

    badgerModel = BadgerModel()
    badgerId = badgerModel.getBadgerIdFromQrId(qrId)

    if badgerId:
        return json.dumps(badgerId)
    else:
        return json.dumps(False)


@app.route('/update_presence', methods=['POST'])
def update_presence():
    jsonBadgerId = json.loads(request.form["id"])
    badgerId = jsonBadgerId["id"]

    roomId = request.form["room"]
    fieldToUpdate = get_field_to_update()

    presenceModel = PresenceModel()
    result = presenceModel.getPresenceByBadgerId(badgerId)
    presenceModel.postPresence(badgerId, roomId, fieldToUpdate)

    return json.dumps(True)


def get_field_to_update():
    now = datetime.datetime.now()

    if now.hour < 12:
        field_to_update = "morning_date"
    else:
        field_to_update = "afternoon_date"
    return field_to_update
