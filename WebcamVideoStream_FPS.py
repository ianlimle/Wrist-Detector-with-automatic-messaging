# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 19:03:16 2018

@author: Ian
"""

import datetime 
from threading import Thread
import cv2

class FPS:
    def __init__(self):
        #store start time, end time and total number of frames
        #that were examined betwwen the start and end intervals
        self._start=None
        self._end=None
        self._numFrames=0
        
    def start(self):
        #start the timer
        self._start=datetime.datetime.now()
        return self
    
    def stop(self):
        #stop the timer
        self._end=datetime.datetime.now()
        
    def update(self):
        #increment the total num of frames examined during the start and end intervals 
        self._numFrames+=1
        
    def elapsed(self):
        #return the total number of seconds betwwen the start and end interval
        return (self._end-self._start).total_seconds()
    
    def fps(self):
        #compute the approximate frames per second
        return self._numFrames/self.elapsed()
    
    
class WebcamVideoStream:
    def __init__(self, src=0):
        #initialize the video camera stream and read the first frame
        #from the stream 
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        
        #initialize the variable used to indicate if the thread should be stopped
        self.stopped = False
        
    def start(self):
        #start the thread to read frames from the video stream 
        Thread(target=self.update, args=()).start()
        return self
    
    def update(self):
        #keep looking infinitely until thread has stopped
        while True:
            #if the thread indicator variable is set, stop the thread
            if self.stopped:
                return 
            
            #otherwise, read the next frame from the stream
            (self.grabbed,self.frame) = self.stream.read()
            
    def read(self):
        #return the frame most recetly used 
        return self.frame

    def stopped(self):
        #indicate that the thread should be stopped
        self.stopped= True        
        
        