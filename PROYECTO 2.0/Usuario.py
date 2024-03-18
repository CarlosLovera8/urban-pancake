from abc import ABC, abstractmethod
import json

class Users(ABC):

     def  __init__(self, id : str,  name : str, email : str, username : str, type : str):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.type = type

        def __str__(self):
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "username": self.username,
                "type": self.type
            }


        def __eq__(self, other):
            if isinstance(other, Users):
                return self.id == other.id
            return False

        def __gt__(self, other):
            if isinstance(other, Users):
                return self.id > other.id
            return False