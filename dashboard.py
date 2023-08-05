import random
from Controller import dashboard_controller

# Initilize dashboard_controller
dashboard_controller = dashboard_controller.Dashboard_controller()


class Dashboard:
     def __init__(self, linklist, favourite_song_diroctory):
          
          
         self.linklist = linklist
         
         
         self.favourite_song_diroctory = favourite_song_diroctory
         
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