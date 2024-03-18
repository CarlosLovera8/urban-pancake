from Usuario import Users

class Listener(Users):
    
    def __init__(self, id, name, email, username, type : str):
        super().__init__(id, name, email, username, type)
        self.likedalb = []
        self.likedsongs = []
        self.playlists = []
        
    def __str__(self):
        return f'''\n{super().__str__()}
                      Liked albums: {self.likedalb}
                      Liked songs: {self.likedsongs}
                      Playlists: {self.playlists}\n'''
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value