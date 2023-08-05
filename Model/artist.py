# Class Artist    
class Artist:
     def __init__(self, name):
         self.name = name
         
         
         
         
         
        #  self.infolist = infolist
        #  self.linklist = linklist

     def Artistlist(self, index = 0):
         artistlist = []
         infolist = self.infolist.splitlines()
         while True:
               try:
                   detail = infolist[index]
                   artistname = detail[0:detail.index("-")-1]
                   if len(artistlist) == 0:
                      if "-" in detail.split()[0]:
                         artistlist.append(detail.split()[0])
                      else:
                           artistlist.append(artistname)         
                   else:
                        if "-" in detail.split()[0]:
                             if detail.split()[0] in artistlist: pass
                             else:
                                  artistlist.append(detail.split()[0])
                        elif artistname in artistlist: pass
                        else:
                             artistlist.append(artistname)
                   index += 1
               except IndexError:
                      break
         return artistlist   

## artist song
     def Artistsonglist(self, songlist, artistlist, index = 0):
         artistsonglist = []
         infolist = self.infolist.splitlines()
         while True:
               try:
                   artistsong = []
                   artistname = artistlist[index]          
                   for info in infolist:
                       if artistname in info:
                          artistsong.append(songlist[infolist.index(info)])                        
                   artistsonglist.append(artistsong)
                   index += 1
               except IndexError:
                      break
         return artistsonglist

# artist song link list
     def Artistsonglinklist(self, artistsonglist, index = 0):
         artistssonglinklist = []
         linklist = self.linklist
         while True:
               try:
                   artistsonglinklist = []
                   artistsong = artistsonglist[index]
                   for songname in artistsong:
                       for link in linklist:
                           if songname in link:
                              artistsonglinklist.append(link)
                   artistssonglinklist.append(artistsonglinklist)
                   index += 1
               except IndexError:
                      break
         return artistssonglinklist
