def makeAlbum(artistName,albumTitle,noOfSongs=None):
    album = {
        "Artist name":artistName.title(),
        "Album title":albumTitle.title()
    }

    if noOfSongs:
        album['Number of songs in album']=noOfSongs
    
    return album

while True:
    print("\nEnter the album details(type 'quit' at any time to leave): ")
    nameArtist=input("Enter the artist name- ")
    if nameArtist=='quit':
        break
    nameAlbum=input("Enter the album name- ")
    if nameAlbum=='quit':
        break

    print(makeAlbum(nameArtist,nameAlbum))
