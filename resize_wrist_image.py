# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:01:51 2018

@author: Ian
"""
import time
import cv2

def resize_image():
    date_yyyymmdd = time.strftime("%Y-%m-%d")
    img = cv2.imread("wrist.jpg",cv2.IMREAD_GRAYSCALE)
    # should be larger than samples / pos pic (so we can place our image on it)
    resized_image = cv2.resize(img, (50, 50))
    for i in range(1,6):
        cv2.imwrite(str(date_yyyymmdd)+"_pic_"+str(i)+".jpg",resized_image)
        
resize_image()            