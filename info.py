# Class Info
class Info:
     def __init__(self, infofolderdirectory, playdirectory):
         self.infofolderdirectory = infofolderdirectory # Info folder
         self.playdirectory = playdirectory # Song file
         
##  song file contain all songs information
     def Infofile(self):
          with open(self.infofolderdirectory, "r") as infofile:
               infofile = open(self.infofolderdirectory, "r")
          infolist = infofile.read()
          return infolist
     
# Play Directory that will play certain song
     def Linklist(self, index = 0):
          linklist = []
          with open(self.infofolderdirectory, "r") as infofile:
               infofile = open(self.infofolderdirectory, "r")
          link = infofile.read().splitlines()
          while True:
                try:
                   linklist.append("{}{}.mp3".format(self.playdirectory, link[index]))
                   index += 1
                except IndexError:
                       break
          return linklist