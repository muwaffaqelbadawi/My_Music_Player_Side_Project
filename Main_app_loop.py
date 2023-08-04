def main():     
     ##objects
     infofolder = Infofolder("D:\\little python projects\Player\infofolder\songfile.txt", "C:\\Users\Muwaffuq\Music\\")
     song = Song(infofolder.Infofile())
     artist = Artist(infofolder.Infofile(), infofolder.Linklist())
     favourite = Favouritesong(infofolder.Linklist())
     lyrics = Lyrics("D:\\little python projects\Player\Lyricsfolder")
     page = Page(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
     function = Function(infofolder.Linklist(), "D:\\little python projects\Player\\Favouritesong\\likefile.txt")
     ui = UserInterface(song.Songlist(), artist.Artistlist(), artist.Artistsonglist(song.Songlist(), artist.Artistlist()))

     ##app body
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
               artistsonglist = artist.Artistsonglinklist(artist.Artistsonglist(song.Songlist(), artist.Artistlist()))
               linklist = artistsonglist[artistindex] # link list
               songlink = linklist[songindex] # song link
               function.Play(songlink) # select button

          elif selection == "likelist":
               songlist = favourite.Likelist() # song list
               print(ui.Show(songlist, "song"))
               songname = input("songname:\n")
               songindex = songlist.index(songname) # song index
               linklist = favourite.Linklist(favourite.Likelist()) # link list
               songlink = linklist[songindex] # song link
               function.Play(songlink) # select button
               
          ## control function
          def control_finction(action):
               return function.Select(function.Push(action))
          
          while True:
               action = input("shuffle\nprevious pause next\nlike resume stop\n")
               control = control_finction(action)
               function.Play(songlink)

if __name__ == "__main__": 
   main()