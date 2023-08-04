# Class Song 
class Song:
     def __init__(self, infolist):
        self.infolist = infolist
        
# Song List                         
     def Songlist(self, index = 0):
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