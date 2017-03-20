# -*- coding: utf-8 -*-
#! /usr/bin/env python
import  picamera
import qrtools
import urllib
from time import sleep
import wiringpi as wpi
import requests


#--------------------------------------------#
#-----------------CONSTANTES-----------------#
#--------------------------------------------#
blink_delay = 2
pin_orange_number = 0
pin_green_number = 1
picture_name = "scan.jpg"
wpi.wiringPiSetup()
wpi.pinMode(1, 1)
room = "Toulouse"

#-------------------------------------------#
#----------------SCAN QR CODE---------------#
#-------------------------------------------#
#Méthode principale: Scan du qr code
#camera = la camera a utilser
#delay = La durée de prise entre 2 images
def scan_qr_code(camera, delay):
    camera.capture(picture_name)
    qr = qrtools.QR()
    #Appel à la vérification de l'existance de l'utilisateur en base
    verify_user(qr, picture_name)
    sleep(delay)

#-------------------------------------------#
#----------------VERIFY USER----------------#
#-------------------------------------------#
#Méthode de vérification de l'utilisateur
#qr = objet permettant le décryptage du qr code
#picture_name = nom des images que prend la camera
def verify_user(qr, picture_name):
    #Décodage QR CODE
    if qr.decode(picture_name):
        result = qr.data
        qr_id = urllib.urlencode({'id': result})
        #Est-ce que l'utilisateur existe ?
        isUserValid = (requests.get("http://raspi.com:8002/verify_user", data={'id': qr_id})).text
        print "USER VALID" + str(isUserValid)

        #Si l'utilisateur existe:
        if isUserValid != "false":
            print "Utilisateur trouvé en base"
            # Si l'utilisateur existe en base, on update la presence
            update_presence(isUserValid)
        else:
            blink_orange();
    else:
        print "QR CODE NON RECONNU"
        return "false"

#-------------------------------------------#
#--------------UPDATE PRESENCE--------------#
#-------------------------------------------#
#Appel l'api qui update la présence de l'utilisateur en base
def update_presence(isUserValid):
   responseApi2 = requests.post("http://raspi.com:8002/update_presence", data={'id': isUserValid, 'room': room})
   print "presence updated ? " + str(responseApi2.text)
   blink_green();

#-------------------------------------------#
#----------------BLINK GREEN----------------#
#-------------------------------------------#
#Clignotement de la led verte
def blink_green():
    wpi.pinMode(pin_green_number, 1)
    wpi.digitalWrite(pin_green_number, 1)
    sleep(blink_delay)
    wpi.digitalWrite(pin_green_number, 0)


#-------------------------------------------#
#----------------BLINK ORANGE----------------#
#-------------------------------------------#
#Clignotement de la led orange
def blink_orange():
    wpi.pinMode(pin_orange_number, 1)
    wpi.digitalWrite(pin_orange_number, 1)
    sleep(blink_delay)
    wpi.digitalWrite(pin_orange_number, 0)
