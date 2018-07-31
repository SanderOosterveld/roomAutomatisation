# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:49:35 2018

@author: Sander Oosterveld
"""
from tkinter import Label
import datetime

class Widget(Label):
    classCounter = 0
    def __init__(self, master, pos, *args, **kwargs):
        '''
        pos should be a Position Object
        '''
        Label.__init__(self, master, *args, **kwargs)
        self.id = Widget.classCounter
        Widget.classCounter += 1
        self.position = pos
        
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    
    def changePosition(self,newPos):
        self.position = newPos
    
    def changeBackground(self, Background):
        self.config(bg = Background)
        
    def make(self):
        print("placing widget at:"+ str(self.position.getXPosition()) + str(self.position.getYPosition()))
        self.place(relx = self.position.getXPosition(), rely = self.position.getYPosition(), anchor = 'center')
    
    def __str__(self):
        return "Widget:" + str(self.id)
    
    def __repr__(self):
        return str(self)
    
    
class TextWidget(Widget):
    def __init__(self, master, pos, widgetText, *args, **kwargs ):
        Widget.__init__(self, master, pos, *args, **kwargs)
        self.root = master
        self.text = widgetText
        self.config(text = self.text)
        self.startTransparent(self.root['bg'])
        self.changeBackground(self.root['bg'])
        

    def getText(self):
        return self.text
    
    def changeText(self, newText):
        '''
        Changes the text shown by widget
        input: String
        output: void
        '''
        self.config(text = newText)

    def changeFont(self, newFont):
        '''
        Change the font of the widget in tuple with font and size
        input: Tuple(String,int)
        '''
        self.config(font = newFont)
        
    def __str__(self):
        return "Textwidget showing: " + self.text
    
    def startTransparent(self, currentBg):
        if currentBg == self.root['bg']:
            self.after(10, self.startTransparent, currentBg)
        else:
            self.changeBackground(self.root['bg'])
            if self.root['bg'] == 'black':
                self.config(fg = 'white')
            else:
                self.config(fg = 'black')
            self.after(500, self.startTransparent, self.root['bg'])
            
        
class TimeWidget(TextWidget):
    
    def __init__(self, master, *args, **kwargs ):
        TextWidget.__init__(self, master, Position(0.5,0.5), "", *args, **kwargs)
        self.changeFont(('Helvetica',32))
        self.updateTime("")
        
    def timeMaker(self):
        currentTime = datetime.datetime.now()
        Second = str(currentTime.second)
        Minute = str(currentTime.minute)
        Hour = str(currentTime.hour)
        if int(Second) < 10 :
            Second = '0'+Second
        if int(Minute) < 10 :
            Minute = '0'+Minute
        if int(Hour) < 10 :
            Hour = '0'+Hour
        return Hour + ':' + Minute + ':' + Second
    
    def updateTime(self, currentTime):
        if self.timeMaker() == currentTime:
            self.master.after(100, self.updateTime, currentTime)
        else:
            newTime = self.timeMaker()
            self.changeText(newTime)
            self.after(500, self.updateTime, newTime)
    
class Position():
    def __init__(self,xpos,ypos):
        self.xPosition = xpos
        self.yPosition = ypos
        
    def getPositionRel(self):
        return (self.xPosition, self.yPosition)
    
    def getXPosition(self):
        return self.xPosition
    
    def getYPosition(self):
        return self.yPosition
    
    def movePositionUp(self,increment):
        self.yPosition -= increment
        
    def movePositionRight(self, increment):
        self.xPosition -= increment
    
    def toPixel(self):
        return (self.xPosition*1280, self.yPosition*720)
        
    def __str__(self):
        return "relX: " + str(self.xPosition)+", relY: "+str(self.yPosition)
    
        