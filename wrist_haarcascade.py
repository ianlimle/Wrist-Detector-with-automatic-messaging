# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 09:06:06 2018

@author: Ian
"""
import requests
import cv2
import json
from imutils.video import FPS
from imutils.video import WebcamVideoStream
import time

def triggered(message):
    url = 'https://bosch-ville-api.unificationengine.com/v1/message/send'
    api_token = 'Y2gmZGV2aWNlX3R5cGU9WERJ'
    headers = {'Content-Type': 'application/json', 'Authorization': api_token}
    body = {"phone_number": "+6590698810", "message":message}
    requests.post(url, data=json.dumps(body), headers=headers)         
    
#this is the cascade we just made. Call what you want
wrist_cascade = cv2.CascadeClassifier('wrist_cascade.xml')

vs = WebcamVideoStream(src=0).start()
time.sleep(1)
fps = FPS().start()


while fps._numFrames <10000:
    #capture frame-by-frame
    img = vs.read()    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    wrist = wrist_cascade.detectMultiScale(gray,50,50)
    
    for (x,y,w,h) in wrist:
        #place a rectangle around object detected 
        print(wrist)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #font = cv2. FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Wrist', (w-x,y-h), font, 0.5,(11,255,255), 2, cv2.LINE_AA)
        triggered("Wrist detected.")

    cv2.imshow('img', img)
    #wait for 1 milisec if the character 'q' is pressed in that duration, quit the program
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
    #update the frames per second 
    fps.update()

fps.stop()        
cv2.destroyAllWindows()
vs.stop()