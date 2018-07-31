# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:05:03 2018

@author: Sander Oosterveld
"""
import pygame
from MainScreen import MainScreen
from queue import Queue
from ConnectionWidget import ConnectionWidget
from MusicPlayer import MusicPlayer
from SocketClient import SocketClient
from Widget import Widget, TextWidget, Position, TimeWidget
from Alarm import Alarm, AlarmWidget
from TimerObject import TimerObject

q = Queue()
screen = MainScreen(q)
timerObject = TimerObject(screen)
timerObject.addObject(screen.changeBackground, ('1900', -1), "black")
timerObject.addObject(screen.changeBackground, ('1901', -1), "white")
screen.start()
