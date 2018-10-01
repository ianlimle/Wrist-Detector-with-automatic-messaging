# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 00:08:34 2018

@author: Ian
"""
import os

def create_pos_n_neg():
    
#    for file_type in ['pos']:
#        
#        for img in os.listdir(file_type):
#            
#            if file_type == 'pos':
#                line = file_type+'/'+img+' 1 0 0 50 50\n'
#                with open('info.txt','a') as f:
#                    f.write(line)
                    
                    
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):                    
                    
            if file_type == 'neg':
                 line = file_type+'/'+img+'\n\n\n'
                 with open('bg.txt','a') as f:
                     f.write(line)
                    
create_pos_n_neg()                      