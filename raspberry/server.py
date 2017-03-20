# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import mysql.connector
import datetime

app = Flask(__name__)


#-------------------------------------------#
#----------------VERIFY USER----------------#
#-------------------------------------------#

#Api de verification de l'existence de l'utilisateur en base
#Si existe: Renvoie id utilisateur
#Si existe pas: Renvoie "false"
@app.route('/verify_user', methods=['GET'])
def api1():
    #Récupération de l'id du qr_code
    request_param = request.form["id"]
    id = request_param.split("=")[1]

    #Requete SQL
    connexion = mysql.connector.connect(host="localhost", user="rasp_user", password="rasp_user", database="mydb")
    curseur = connexion.cursor()
    curseur.execute('Select id from badger WHERE badger.qr_id = "'+id+'" ')
    result = curseur.fetchall()
    connexion.close()

    #Return les résultats
    if len(result)!= 0:
        return json.dumps(result[0][0])
    else:
        return json.dumps(False)

# -------------------------------------------#
# --------------UPDATE PRESENCE--------------#
# -------------------------------------------#

#Met a jour la table presence de l'utilisateur
@app.route('/update_presence', methods=['POST'])
def api2():
    #Récupération de l'id de l'utilisateur a updater
    id = request.form["id"]
    print id
    room = request.form["room"]
    print room
    room_id = get_room_id(room)
    print room_id
    fieldToUpdate = get_field_to_update()
    print fieldToUpdate

    #Requete SQL- Varie en fonction de si on est le matin ou l'aprem, et si l'utilisateur
    #est dans la table présence ou non
    connexion = mysql.connector.connect(host="localhost", user="rasp_user", password="rasp_user", database="mydb")
    curseur = connexion.cursor(buffered=True)
    curseur.execute('SELECT * FROM presence WHERE badger_id = "' + id + '"')

    #Si l'utilisateur n'est pas dans la table présence: on INSERT
    if not curseur.rowcount:
        try:
            curseur.execute('INSERT INTO presence (badger_id, room_id, "' + fieldToUpdate + '") VALUES("' + id + '" ,"' + room_id + '", CURRENT_TIMESTAMP)')
        except mysql.connector.Error:
            print "LED rouge sur l'insert"

    #Sinon, on UPDATE l'utilisateur
    else:
        try:
           curseur.execute('UPDATE presence SET ' + fieldToUpdate + ' = CURRENT_TIMESTAMP WHERE badger_id = "' + id + '"')
        except mysql.connector.Error:
           return json.dumps(False)
           print "LED rouge sur l'update"
    connexion.commit()
    connexion.close()

    #Return les résultats
    return json.dumps(True)


#-------------------------------------------#
#------------GET FIELD TO UPDATE------------#
#-------------------------------------------#

#Permet de savoir si l'utilisateur badge le matin ou l'aprem
def get_field_to_update():
    #Récupération de l'heure actuelle
    now = datetime.datetime.now()
    print "heure actuelle: " + str(now.hour)

    #On détermine si on est le matin ou l'après midi
    if now.hour < 12:
        field_to_update = "morning_date"
    else:
        field_to_update = "afternoon_date"
    return field_to_update

def get_room_id(room):
    connexion = mysql.connector.connect(host="localhost", user="rasp_user", password="rasp_user", database="mydb")
    curseur = connexion.cursor(buffered=True)
    curseur.execute('SELECT id FROM room WHERE name = "' + room + '"')

    result = curseur.fetchall()
    connexion.commit()
    connexion.close()
    return result[0][0]


if __name__ == '__main__':
    print "started v1.3"
    app.run(host='', port=8002,debug=True,threaded=True)

