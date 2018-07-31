# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 18:42:53 2018

@author: Sander Oosterveld
"""

from MainScreen import MainScreen
from Alarm import Alarm, AlarmWidget
from queue import Queue
from Widget import TimeWidget, TextWidget, Position
from TimerObject import TimerObject

q = Queue()
screen = MainScreen(q)
screen.changeBackground('white')
alarm = Alarm("0700", "disturbed.ogg", True)
alarmWidget = AlarmWidget(screen, alarm)
timeWidget = TimeWidget(screen)
alarmWidget.make()
timeWidget.make()

timerObject = TimerObject(screen)
timerObject.addObject(screen.changeBackground, ("2300", -1), "black")
timerObject.addObject(screen.changeBackground, ("0630", -1), "white")
timerObject.addObject(alarm.activate, ("0600", -1))

screen.start()
