# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:58:27 2018

@author: mlsv.slv.eda.in.IL
"""

import cv2
import glob
import os

def process_raw_images():
    
    pospath = 'C:/Users/Ian/Desktop/positives_raw'
    pic_num =1
    
    if not os.path.exists('pos'):
        os.mkdir('pos')
        
    for infile in glob.glob(os.path.join(pospath, '*.*')):
        
        if infile.split(".")[-1].lower() in {"jpg"}:
            
            img = cv2.imread(str(infile), cv2.IMREAD_GRAYSCALE)
            #resize images 
            resized_image = cv2.resize(img, (50,50))
            #save resized images 
            cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
process_raw_images()
                    
                    
                    
