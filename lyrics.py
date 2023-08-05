# Class Lyrics
class Lyrics:
     def __init__(self, name):
          self.name = name
          
          
          
          






     def Show(self, songlist, songindex):
         lyricsfolderdirectory = self.lyricsfolderdirectory
         lyricsname = songlist[songindex]
         lyricsfiledirectory = "{}\{}.txt".format(lyricsfolderdirectory, lyricsname)
         with open(lyricsfiledirectory, "r") as lyricsfile:
              lyricsfile = open(lyricsfiledirectory, "r")
         lyrics = lyricsfile.read()
         return "\n{}\nThe End\n".format(lyrics)
