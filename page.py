# Class Page
class Page:
     def __init__(self, songlist, artistlist, artistsonglist):
         self.songlist = songlist
         self.artistlist = artistlist
         self.artistsonglist = artistsonglist
         
         
         
         
         
         
     def Artistsongpage(self, pageindex): 
         print("\n{}:".format(self.artistlist[pageindex]))
         artistsonglist = self.artistsonglist[pageindex]
         return artistsonglist