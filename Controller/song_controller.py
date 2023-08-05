# Here's where the logic of song kept

import os
from os import path


class Song_Controller:
    
    
    @classmethod
    def Loader():
        pass
    
    
    
    @classmethod
    def Delete(song, entered_song):
        return True if song != entered_song else False
    
    
    
    @classmethod
    # Song List                         
    def Songlist(index = 0):
        songlist = []
        infolist = self.infolist.splitlines()
        while True:
            try:
                detail = infolist[index]
                songname = detail[detail.index("-")+2:len(detail)]
                if "-" in detail.split()[0]:
                    songlist.append(detail[len(detail.split()[0])+3:len(detail)])
                else:
                    songlist.append(songname)
                index += 1                       
            except IndexError:
                    break
        return songlist