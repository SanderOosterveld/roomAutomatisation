# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:31:53 2018

@author: Sander Oosterveld
"""

import pygame as pg
import time

class MusicPlayer():
    
    def __init__(self, musicFile):
        '''
        object uesd to play music
        the input is a string with the music file
        '''
        pg.mixer.init()
        pg.mixer.music.load(musicFile)
        self.musicFile = musicFile
        
    def start(self):
        pg.mixer.music.play()
        
    def shutdown(self):
        pg.mixer.quit()
        
    def pause(self):
        pg.mixer.music.pause()
        
    def unpause(self):
        pg.mixer.music.unpause()
        
    def newSong(self, newMusicFile):
        '''
        Loads a new song and starts playing it
        '''
        
        try:
            pg.mixer.music.load(newMusicFile)
        except:
            print("music file could not be loaded")
        self.musicFile = newMusicFile
        pg.mixer.music.play()
        
    def getSong(self):
        
        return self.musicFile
