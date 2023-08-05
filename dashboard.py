# Class Dashboard
# import pygames



import random
class Dashboard:
     def __init__(self, linklist, favouritesongdiroctory):
         self.linklist = linklist
         self.favouritesongdiroctory = favouritesongdiroctory
         
     # def Play(self, songlink):
     #     pygame.mixer.init()
     #     pygame.mixer.music.load(songlink)
     #     pygame.mixer.music.play()
         
     def Select(self, select):
         if type(select) is str:
            for link in self.linklist:
                if select in link:
                   songlink = link
                   return songlink
                if select == "shuffle":
                     songlink = random.choice(self.linklist)
                     return songlink                    
                elif select == "previous":
                     songlink = self.linklist
                     return songlink    
                elif select == "next":
                     songlink = self.linklist
                     return songlink
                else:
                     return select
                    
     # def Push(self, push):
     #     if push == "pause":
     #          pygame.mixer.music.pause()
     #     elif push == "resume":
     #          pygame.mixer.music.unpause()
     #     elif push == "stop":
     #          pygame.mixer.music.stop()
     #     else:
     #          return push
