# Class Favorite
class Favouritesong:
     def __init__(self, songlinklist):
        self.linklist = songlinklist
        
     def Likelist(self, index = 0):
         with open(self.favouritesongdiroctory) as likefile:
              likefile = open(self.favouritesongdiroctory, "r")
         filelist = likefile.readlines()
         likelist = []
         while True:
               try:
                   likelist.append(filelist[index].strip("\n"))
                   index += 1      
               except IndexError:
                      break
         return likelist

# like song link list
     def Linklist(self, likelist, index = 0):
         linklist = []
         while True:
               try:
                   songname = likelist[index]
                   for link in self.linklist:
                       if songname in link:
                          linklist.append(link)
                   index += 1
               except IndexError:
                      break
         return linklist
