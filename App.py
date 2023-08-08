# This is the main Class Index of the app
# Always remember to use snake_case with python

# I made changing in App.py
# #######################

from Model import song, artist, favorite, info, dashboard, lyrics, page, UI

song = song.Song()
artist = artist.Artist()
favorite = favorite.Favorite()
info = info.Info()
dashboard = dashboard.Dashboard()
lyrics = lyrics.Lyrics()
page = page.Page()
UI = UI.UserInterface()

# Main App
class App:
     def __init__(self) -> None:
          pass


     def app_loop():
          info_folder = info()
          
          song_object = song(info.Infofile())
          
          artist_object = artist(info.Infofile(),
                                 info.Linklist())
          
          favorite_object = favorite(info.Linklist())
          
          lyrics_object = lyrics()
          
          page_object = page(song.Songlist(),
                             artist.Artistlist(),
                             artist.Artistsonglist(song.Songlist(),
                                                   artist.Artistlist()))
          
          function = dashboard(info.Linklist())
          
          ui = UI(song.Songlist(),
                              artist.Artistlist(),
                              artist.Artistsonglist(song.Songlist(),
                                                    artist.Artistlist()))

          while True:
               selection = input("songs artists likelist\n")

               if selection == "songs":
                    songlist = song.Songlist() # song list
                    print(ui.Show(songlist, "songs"))
                    songname = input("songname:\n") # song name
                         
                    songindex = songlist.index(songname) # song index
                    function.Play(songlink) # select button

               elif selection == "artists":
                    artistlist = artist.Artistlist() # artist list
                    
                    print(ui.Show(artistlist, "artists"))
                    
                    artistname = input("artistname:\n") # artist name
                    
                    artistindex = artistlist.index(artistname) # artist index
                    
                    songlist = page.Artistsongpage(artistindex) # song list
                    
                    print(ui.Show(songlist, "songs"))
                    
                    songindex = songlist.index(input("songname:\n")) # song index
                    
                    
                    artistsonglist = artist.Artistsonglinklist(artist.Artistsonglist(song.Songlist(),
                                                                                     artist.Artistlist()))
                    
                    linklist = artistsonglist[artistindex] # link list
                    
                    songlink = linklist[songindex] # song link
                    
                    function.Play(songlink) # select button

               elif selection == "likelist":
                    songlist = favorite.Likelist() # song list
                    
                    print(ui.Show(songlist, "song"))
                    
                    songname = input()
                    
                    songindex = songlist.index(songname) # song index
                    
                    linklist = favorite.Linklist(favorite.Likelist()) # link list
                    
                    songlink = linklist[songindex] # song link
                    
                    function.Play(songlink) # select button
                    
               ## control function
               def control_finction(action):
                    return function.Select(function.Push(action))
               
               while True:
                    action = input()
                    control = control_finction(action)
                    function.Play(songlink)

if __name__ == "__main__": 
   App()