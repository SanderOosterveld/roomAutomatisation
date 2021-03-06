# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:17:48 2018

@author: Sander Oosterveld
"""

from Widget import TextWidget, Position
#from MainScreen import MainScreen
from MusicPlayer import MusicPlayer
import datetime

class AlarmWidget(TextWidget):
    
    def __init__(self, master, alarm, *args, **kwargs):
        TextWidget.__init__(self, master, Position(0.95,0.01),"alarm set at: " + alarm.getTime(), *args, **kwargs)
        self.root = master
        self.alarm = alarm
        self.allAlarms = [self.alarm]
        self.musicPlayer = MusicPlayer(alarm.getSound()) 
        self.alarmLength = 20
        self.startChecker()
        
    
    def getAlarmLength(self):
        return self.alarmLength
    
    def setAlarmlength(self, seconds):
        self.alarmLength = seconds
            
    def setNewAlarm(self, alarm):
        self.allAlarms.append(alarm)
        
    def notifyNewAlarm(self, alarm):
        self.changeText("Alarm set at" + alarm.getTime())
        self.make()
        self.root.after(3000, self.place_forget)
        
        
    def alarmProtocol(self, seconds, alarm, repeats):
        def colourChanger(flag, counter, maxCounter):
            if counter < maxCounter:
                if flag == True:
                    self.root.changeBackground('white')
                    newCounter = counter + 1
                    self.root.after(500, colourChanger, False, newCounter, maxCounter)
                else:
                    self.root.changeBackground('black')
                    newCounter = counter + 1
                    self.root.after(500, colourChanger, True, newCounter, maxCounter)
            else:
                self.root.changeBackground('white')
                if repeats > 0:
                    self.root.after(30000, self.alarmProtocol, self.getAlarmLength(), Alarm(alarm.getTime(), alarm.getSound(), True), repeats-1)
                
        
        colourChanger(True, 0, seconds*2)
        self.musicPlayer.newSong(alarm.getSound)
        self.root.after(seconds*1000, self.musicPlayer.pause)
        
        
    def startChecker(self):
        '''
        Starts Checking the alarm
        '''
        self.__alarmChecker()
        
    def __alarmChecker(self):
        '''
        starts an infinite loop checking for an alarm
        '''
        stringTime = self.__timeMaker()
        timeToAlarm = {}
        for alarm in self.allAlarms:
            timeToAlarm[alarm.getTime()] = alarm
        if stringTime in timeToAlarm.keys():
            possibleAlarm = timeToAlarm[stringTime]
            if possibleAlarm.getActivity():
                self.alarmProtocol(self.getAlarmLength(), timeToAlarm[stringTime], 1)
                possibleAlarm.deactivate()
        self.after(6000, self.__alarmChecker)
                
        
    def __timeMaker(self):
        currentTime = datetime.datetime.now()
        hour = str(currentTime.hour)
        minute = str(currentTime.minute)
        if int(minute) < 10 :
            minute = '0'+minute
        if int(hour) < 10 :
            hour = '0'+hour
        
        return hour+minute
    
    def stop(self):
        self.destroy()
        self.musicPlayer.shutdown()
    
    def __str__(self):
        return "AlarmWidget present"
            
class Alarm():
    
    def __init__(self, time, song, active):
        '''
        ALarm object needing three very specific entries
        String time  (e.g. 0700, 2354)
        String song (e.g disturbed.ogg)
        Boolean active (e.g. False or True)
        '''
        
        self.time = time
        self.sound = song
        self.active = active
        self.repeat = False
        
    def setRepeat(self, condition):
        '''
        adds a repeat statement, if the repeat needs to be removed enter False.
        
        format = <tuple of days 0 = monday> e.g. (0,1,2,3,4) to set alarm every weekday
        '''
        self.repeat = condition    
    
    def getRepeat(self):
        return self.repeat
        
        
    def setAlarmSong(self, alarmSong):
        self.sound = alarmSong
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
        
    def changeTime(self, newTime):
        self.time = newTime
        
    def getActivity(self):
        return self.active
    
    def getTime(self):
        return self.time
    
    def getSound(self):
        return self.sound
    
    
    def timeMaker(self, hour, minute):
        if hour<10:
            stringHour = '0'+str(hour)
        else:
            stringHour = str(hour)
        
        if minute < 10:
            stringMinute = '0' + str(minute)
        else:
            stringMinute = str(minute)
        
        return stringHour + stringMinute
        
        
    def addTime(self, addedMinutes):
        '''
        adds a couple minutes to the alarm and returns the new time
        '''
        currentMinutes = int(self.time[2:4])
        currentHours = int(self.time[0:2])
        newMinutes = (addedMinutes+currentMinutes)%60
        addedHours = int((addedMinutes+currentMinutes)/60)
        newHours = (currentHours+addedHours)%24
        return self.timeMaker(newHours, newMinutes)
    
    
    def __str__(self):
        return self.getTime() + ':' + str(self.getRepeat()) + ':' + self.getSound() + ':' + str(self.getActivity())
    
    
#some fun comments      