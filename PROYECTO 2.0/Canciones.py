class Songs:
    def __init__ (self, id : str, name : str, duration : str, link : str, likes : int, description : str):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link  # Link to the song on internet
        self.likes = likes   # Quantity of  people that liked this song
        self.description = description
        
    def __str__ (self):
        return f'''\n Songs (ID: {self.id}
                      Name: {self.name}
                      Duration: {self.duration}
                      Link: <a href="{self.link.href}">{self.link.href}</a>
                      Likes: {self.likes})\n'''
                      
    def __iter__(self):
        return iter([self])
    
    def add_like(self):
        self.likes += 1

    def remove_like(self):
        self.likes -= 1

    def get_likes(self):
        return self.likes

    def get_description(self):
        return self.description