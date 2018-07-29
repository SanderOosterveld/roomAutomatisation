# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:57:35 2018

@author: Sander Oosterveld
"""

from Widget import TextWidget, Position
from SocketClient import SocketClient

class ConnectionWidget(TextWidget):
    
    def __init__(self, master, address, *args, **kwargs ):
        TextWidget.__init__(self, master, Position(0.5,0.1), address, *args, **kwargs)
        self.changeFont(("Helvetica", 16))
        
    def updateConnection(self, client):
        self.changeText(client.getConnectionData())
        self.after(500, self.updateConnection, client)