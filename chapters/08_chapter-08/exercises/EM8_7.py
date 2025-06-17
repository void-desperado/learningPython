def makeAlbum(artistName,albumTitle,noOfSongs=None):
    album = {
        "Artist name":artistName.title(),
        "Album title":albumTitle.title()
    }

    if noOfSongs:
        album['Number of songs in album']=noOfSongs
    
    return album