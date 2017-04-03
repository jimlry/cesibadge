# -*- coding: utf-8 -*-
#! /usr/bin/env python
import  picamera
import takePhoto_method

camera = picamera.PiCamera()
delay = 3

while True:
    takePhoto_method.scan_qr_code(camera, delay);
camera.close()
