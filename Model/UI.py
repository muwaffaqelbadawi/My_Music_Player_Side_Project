from Controller import UI_controller

# Initilize UI_controller
UI_controller = UI_controller.UI_controller()



class UserInterface:
     def __init__(self, songlist, artistlist, artistsonglist):
         self.songlist = songlist
         self.artistlist = artistlist
         self.artistsonglist = artistsonglist



     def Show(self, List, gener, index = 0): 
         while True:
               try:
                   print(List[index])
                   index += 1
               except IndexError:
                      break
         return "{} {}\n".format(len(List), gener)
     
     
     
     
     def Playingnow(self, songlink, songlist, artistlist):
         pass