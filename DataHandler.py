# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:31:13 2018

@author: Sander Oosterveld
"""
#from Alarm import Alarm

class DataHandler():
    
    def __init__(self):
        self.background = 'white'
        self.alarms = []
        self.toDos = {}
        self.lightMode = 'None'
        self.modified = [False]
    
    def addData(self, data):
        '''
        This adds the data, the data has to be a string in the following way: (type of data):(value)|(type of data):(value) etc.
        '''
        dataTypes = data.split('|')
        stringToFunction = {
                'BackgroundColour' : (self.setBackground, self.getBackground),
                'AddAlarm' : (self.addAlarm, self.getAlarms),
                'RemoveAlarm' : (self.removeAlarmTime, self.getAlarms),
                'SetAlarmTimeActivity' : (self.AlarmTimeActivity, self.getAlarms),
                'AddToDo' : (self.addToDo, self.getToDo)         
                }
        for dataType in dataTypes:
            splitData = dataType.split(':')
            function = stringToFunction[splitData[0]]
            setFunction = function[0]
            getFunction = function[1]
            if splitData[0] == 'SetAlarmTimeActivity':
                arguments = splitData[1].split(',')
                setFunction(arguments[0],arguments[1])
            else:
                setFunction[0](splitData[1])
                
            self.modified.append = getFunction
            self.modified[0]= True
            
        
    
    def setModifiedFalse(self):
        self.modified = [False]

    def getModified(self):
        return self.modified
    
    
    def getBackground(self):
        return self.background
    
    def setBackground(self, newBackground):
        self.background = newBackground
        
    def addAlarm(self, alarm):
        self.alarms.append(alarm)
    
    def removeAlarmTime(self, alarmTime):
        flag = False
        for alarm in self.alarms:
            if alarm.getTime() == alarmTime:
                self.alarms.remove(alarm)
                flag = True

        if flag == False:
            print("alarmTime not in dataHandler")
                
    def setAlarmTimeActivity(self, alarmTime, activity):
        flag = False
        for alarm in self.alarms:
            if alarm.getTime() == alarmTime:
                if activity:
                    alarm.activate()
                    flag = True
                else:
                    alarm.deactivate()
                    flag = True
                    
        if flag == False:
            print("alarmTime not in dataHandler")      
    
    def getAlarms(self):
        return self.alarms
    
    def setLightMode(self, newLightMode):
        self.lightMode = newLightMode
    
    def getLightMode(self):
        return self.lightMode
    
    def addToDo(self, toDo):
        def findKey():
            keys = self.toDos.keys()
            keys.sort()
            for i in range(len(keys)-1):
                if keys[i] != keys[i+1]-1:
                    return keys[i]+1   
            return keys[-1]+1    
        
        self.toDos[findKey()] = toDo
        
    def getToDo(self):
        return self.toDos
        
        