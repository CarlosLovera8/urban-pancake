import urllib
from Canciones import Songs
from Usuario import Users

class Albums:
    def __init__(self, id: str, name: str, description : str, cover : str, published : str, genre : str, artist, tracklist):
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = Users.id = artist
        self.tracklist = tracklist   
             
    def __str__(self):
        return f'''\n Albums (ID: {self.id}
                      Name: {self.name}
                      Description: {self.description}
                      Cover: {self.cover}
                      Published: {self.published}
                      Genre: {self.genre}
                      Artist: {self.artist}
                      Tracklist: \n{self.tracklist}\n'''
    
    def add_songs():
        pass