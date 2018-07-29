# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:10:21 2018

@author: Sander Oosterveld
"""

from MainScreen import MainScreen
from Widget import TextWidget, Position
from SocketClient import SocketClient
from queue import Queue
from ConnectionWidget import ConnectionWidget


q = Queue()
data = {'BackgroundColour':'white'}
screen = MainScreen(q)
widget1 = TextWidget(screen, Position(0.5,0.5), 'hello')
widget2 = TextWidget(screen, Position(0.5,0.5), 'hello')
widget1.make()
print([widget1, widget2])
socket = SocketClient('130.89.226.101', 51234, q, data)
connectionWidget = ConnectionWidget(screen, socket.getConnectionData())
connectionWidget.make()
connectionWidget.updateConnection(socket)
socket.start()
screen.start()
socket.join()
