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


modified = []
modified = False

if not modified:
    print('this is possible')
    modified = ["hello"]

if not modified:
    print('Weird stuff')
else:
    print('regular stuff')