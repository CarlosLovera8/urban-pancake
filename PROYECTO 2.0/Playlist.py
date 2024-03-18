from Usuario import Users
from Canciones import Songs

class Playlist(Songs):
    def __init__(self,  id : str, name : str, description : str, creator, tracks):
        self.id = id
        self.name = name
        self.description =  description
        self.creator = creator
        self.tracks = tracks

    def add_songs():
        pass