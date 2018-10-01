# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 05:26:52 2018

@author: Ian
"""
import cv2
import numpy as np
import os

def find_uglies():
    
    for file_type in ['neg']:                    #
        for img in os.listdir(file_type):        # start iterating thru all images in the directory
            for ugly in os.listdir('uglies'):
               
                try:
                    current_image_path = str(file_type)+'/'+str(img)       #file_type is the directory path and img is the image path
                    ugly = cv2.imread('uglies/'+str(ugly))                 #this is the ugly image  
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):      #if dimensions are the same _xor is either one or the other; the images are identical 
                        print( "Deleting ugly pic")
                        print("\n")
                        print(current_image_path)
                        os.remove(current_image_path)
                        
                except Exception as e:
                    print(str(e))      
                    
find_uglies()                    