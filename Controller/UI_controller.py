# This is a user interface controller where I can conroll
# all what happen on the user interface

# from pathlib import Path
# import os 
from os import path
# dir_path = os.path.dirname(os.path.realpath(__file__))



class UI_controller:
    def __init__(self):
        pass
    
    @classmethod
    def show_song() -> None:
        pass
    
    @classmethod
    def show_artist() -> None:
        pass
    
    
    
    
    @classmethod
    def show_lyrics(songlist, songindex) -> None:
        
        #  lyricsfolderdirectory = lyrics_folder_directory
         
         lyrics_name = songlist[songindex]
         
         lyrics_file_directory = "{}\{}.txt".format()
         
         with open(lyrics_file_directory, "r") as lyricsfile:
              lyricsfile = open(lyrics_file_directory, "r")
              
         lyrics = lyricsfile.read()
         return "\n{}\nThe End\n".format(lyrics)
    
    
    
    
    @classmethod
    def show_dashboard() -> None:
        pass


    @classmethod
    def show_info() -> None:
        pass