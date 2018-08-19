# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 12:33:36 2018

@author: Sander Oosterveld
"""
import threading
import socket
import datetime
import time

class LightChanger (threading.Thread):
    def __init__(self, hostname, port):
        '''
        Initiates the thread object needs to have:
        Input: hostname(string which is sanderroom.student.utwente.nl), port(50000>x>65535), queue opbject and a DataHandler object
        '''
    
        threading.Thread.__init__(self)      
        self.hostname = hostname
        self.port = port
        self.connected = False
    def run(self):
        print("started thread")
        while True:
            try:
                print("Trying to make socket")
                mySocket = socket.socket()
                print("socket made")
                mySocket.bind((self.hostname,self.port))
                print("socket bound")
                mySocket.listen(1)
                print("socket listening")
                conn, addr = mySocket.accept()
                self.connectedAddress = addr
                print('starting connection')
                passwd = str(conn.recv(1024).decode())
                print(passwd)
                if str(passwd) in self.makeCodes():
                    print("connected")
                    while True:
                        self.connected = True
                        data = conn.recv(1024).decode()
                        if not data:
                            break
                        print("received message: " + str(data))
                    print("Socket being closed")
                    conn.close()
                    self.connected = False
                    #break
                else:
                    print("password not correct")
                    conn.close()
                    self.connected = False
                    time.sleep(5)
            except KeyboardInterrupt:
                self.connected = False
                break
            except OSError:
                print("Adress still in use")
                self.connected = False
                time.sleep(5)
            except:
                print(i)
                time.sleep(4)
        print("outside while loop")
        self.connected = False
            
                
            
    def makeCodes(self):
        currentTime = datetime.datetime.now()
        day = currentTime.day
        #print(day)
        hour = currentTime.hour
        #print(hour)
        minute = currentTime.minute
        #print(minute)
        second = currentTime.second
        if hour >= 12:
            hour = hour-12
        
        #print(hour)
        secondTens = int(second/10)
        possibleSeconds = [secondTens-1,secondTens,secondTens+1]
        codes = []
        for seconds in possibleSeconds:
            #print(seconds)
            intCode = (1213*(day+1)*100000643*(hour+1)*4124473*(minute+1)*8456876119*(seconds+1))**13
            #print(intCode)
            longCode = hex(intCode)
            #print(longCode)
            codes.append(longCode[17:295])
        #print(codes)
        return codes
    
    def getConnectionData(self):
        if self.connected:
            try:
                return "Connected with: " + str(self.connectedAddress)
            except:
                return "No adress --> no connection"
        else:
            return "Phone not Connected"
            
    def testConnected(self):
        return self.connected
    
    
newSocket = LightChanger("sanderroom.student.utwente.nl", 51234)
newSocket.start()