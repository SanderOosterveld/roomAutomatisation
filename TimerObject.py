# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:56:18 2018

@author: Sander Oosterveld
"""

import datetime

class TimerObject():
    
    def __init__(self, master):
        self.master = master
        self.allObjects = {}
        self.run()
    
    def addObject(self, function, conditions, args = "No argument"):
        '''
        function which should be executed at a certain time
        conditions in following format: (string time(e.g.: 2300), tuple with days of the week monday =0(e.g.  (1,2,5), -1) -1 for all days)
        Total would be addObject(screen.changeBackground, (2300,-1), "Black") to change screen to black every day at 23h
        '''
        
        if function not in self.allObjects:
            self.allObjects[function] = [(conditions, args)]
            print(self.allObjects)
        else:
            self.allObjects[function].append((conditions, args))
            print(self.allObjects)
    
    
    def run(self):
        if len(self.allObjects) > 0:
            print(self.allObjects)
            for func in self.allObjects:
                print(self.allObjects[func])
                for argument in self.allObjects[func]:
                    print("testing")
                    condition = argument[0]
                    args = argument[1]
                    
                    if self.checkCondition(condition):
                        if args == "No argument":
                            try:
                                func()
                            except:
                                print("Either function not correct or not good arguments...")
                        else:
                            try:
                                func(args)
                            except:
                                print("Either function not correct or not good arguments...")
                
        self.master.after(3000, self.run)
            
            
    def checkCondition(self, condition):
        setTime = condition[0]
        days = condition[1]
        
        currentTime = datetime.datetime.now()
        hour = currentTime.hour
        if hour<10:
            hour = '0'+str(hour)
        else:
            hour = str(hour)
            
        
        day = currentTime.weekday()
        minute = currentTime.minute
        if minute<10:
            minute = '0'+str(minute)
        else:
            minute = str(minute)
            
        if days == -1:
            correctDay = True     
        elif day in days:
            correctDay = True
        else:
            return False
        
        
        if correctDay:
            if setTime[0:2] == hour:
                if setTime[2:4] == minute:
                    return True
        
        return False
                
        
    def getObjects(self):
        return self.allObjects
    
    def removeFunction(self, function):
        if function in self.allObjects:
            del self.allObjects[function]
            print(self.allObjects)
        else:
            print("Function not on a timer")
        