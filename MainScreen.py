# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:30:51 2018

@author: Sander Oosterveld
"""
#Some import required to have the Screen work
from tkinter import *
#from Widget import TextWidget, Position
import queue
from Alarm import Alarm
#import pygame
#from DataHandler import DataHandler

class MainScreen(Tk):
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.fullscreen = False
        self.screenWidth = 1280
        self.screenHeight = 720  
        self.geometry('%dx%d' % (int(self.screenWidth), int(self.screenHeight)))
        self.switchFullscreen()
        self.allWidgets = []
        self.bind("<Escape>",self.switchFullscreen)
        self.readData()
        
        #starting music services...
        
        
        
    def switchFullscreen(self, *args):
        '''
        sets the screen to full screen
        '''
        if self.fullscreen == False:
            self.attributes('-fullscreen', True)
            self.fullscreen = True
        else:
            self.attributes('-fullscreen', False)
            self.fullscreen = False
        
        
    def changeSize(self, width, height):
        '''
        Needs to numbers and changes the size of the screen
        this can only be observed if the screen is not in fullscreen
        '''
        self.screenWidth = int(width)
        self.screenheight = int(height)
        self.geometry('%dx%d' % (self.screenWidth,self.screenHeight))
        
    def start(self):
        '''
        Starts to show the screen needs to be called at the final end
        '''
        self.mainloop()
        
    def addWidget(self,widget):
        '''
        Adds a widget
        input: Widget Opbject
        output: void
        '''
        try:
            widget.make()
            self.allWidgets.append(widget)
        except(AttributeError):
            print("input was not a widget")
            
    def removeWidget(self, widget):
        '''
        removes a Widget
        input: Widget (sub)Class
        output: void
        '''
        try:
            widget.destroy()
            self.allWidgets.remove(widget)
        except(AttributeError):
            print("Widget was not correctly specified")
        
    def clearScreen(self):
        '''
        clears the screen
        input: void
        output: void
        '''
        for widget in self.allWidgets:
            widget.destroy()
            self.allWidgets.remove(widget)
        
    def printWidgets(self):
        totalString = ""
        for widget in self.allWidgets:
            totalString = totalString + str(widget) +"\n"
        print(totalString)
        
    def readData(self, *args):
        #print("trying to get data")
        def changeBackground(newBackground):
            self.changeBackground(newBackground)
            
        def setAlarm(alarmTime):
            alarm = Alarm(alarmTime, 'disturbed.ogg', True)
            for child in self.winfo_children():
                if str(child) == 'AlarmWidget present':
                    child.addAlarm(alarm)
        
        

                
        
        
        try:
            dataHandler = self.queue.get(0)
            
            if dataHandler.getModified()[0]:
                for function in dataHandler.getModified():
                    dataHandler.function()
                    
                    
                    
                self.after(1000,self.readData)
        except queue.Empty:
            self.after(1000,self.readData)
        
    def changeBackground(self, colour):
        '''
        Changes the Background Colour
        input: string with the colour
        '''
        self.configure(background = colour)
        