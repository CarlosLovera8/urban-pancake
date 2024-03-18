from Usuario import Users

class Musician(Users):
    def __init__(self, id, name, email, username, type : str):
        super().__init__(id, name, email, username, type)
        self.albums = []
        self.top10 = []
        self.reprod = int
        
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
        
    def __str__(self):
        return f'''\n{super().__str__()}
                      Albums: {self.albums}
                      Most listened songs: {self.top10}
                      Reproductions: {self.reprod}\n'''