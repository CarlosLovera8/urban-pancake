from Escucha import Listener
from Usuario import Users
from Musico import Musician
from Canciones import Songs
from Albumes import Albums
from Playlist import Playlist
import json
import uuid
import datetime

class App:
    def __init__(self):
        self.musicians = []
        self.listeners = []
        self.users_data = []
        self.albums = []
        self.tracklist = []
        self.songs = []
        self.playlists = []
        self.likedalb = []
        self.likedsongs = []
        self.top10 = []
        self.current_user = None
        self.active_user = None
        self.load_users()

    def load_users(self):
        with open('PROYECTO 2.0//users.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        # Convertir los diccionarios cargados desde el archivo JSON en objetos de la clase Users
        self.users_data = [Users(**user) for user in user_data]

        # Ordenar los usuarios según su tipo
        self.sort_users()
        
    def load_albums(self):
        with open('PROYECTO 2.0//albums.json', 'r', encoding='utf-8') as f:
            albumz = json.load(f)
        self.albums = [Albums(**alb) for alb in albumz]
        
    def load_playlist(self):
        with open('PROYECTO 2.0//playlists.json', 'r', encoding='utf-8') as f:
            pl = json.load(f)
        self.playlists = [Playlist(**pls) for pls in pl]
        
    def print_users(self):
        for user in self.users_data:
            print(user)

    def sign_up(self):
        id = str(uuid.uuid4())
        name = input('Enter your name: ')
        email = input('Enter your e-mail: ')
        while not '@'in email:
            print('Invalid email')
            email = input('Enter your e-mail: ')
        type = input('Enter your user type:\n1 - Musician\n2 - Listener\n')
        if type == "1":
            type = 'musician' #musician
        elif type == "2":
            type = 'listener' #listener
        username = input('Enter your username: ')

        user = {'id' : id, 'name' : name, 'email' : email, 'username' : username, 'type' : type}
        user_str = json.dumps(user)
        self.write_user_to_txt(user_str)
        print(self.users_data)

        print(f'Welcome {name}')

    def save_albums_to_txt(self):
        with open("albums.txt", "w", encoding="utf-8") as f:
            album_list_str = ""
            for album in self.albums:
                album_dict = {"id": album.id, "name": album.name, "description": album.description, "cover": album.cover, "published": album.published, "genre": album.genre, "artist": album.genre, "tracklist": album.tracklist}
                album_dict_str = json.dumps(album_dict)
                album_list_str += album_dict_str + "\n"
            f.write(album_list_str)
            
    def save_playlists_to_txt(self):
        with open('playlists.txt', 'w', encoding='utf-8') as f:
            playlist_list_str = ""
            for playlizt in self.playlists:
                pl_dict = {'id': playlizt.id, 'name': playlizt.name, 'description': playlizt.description, 'creator': playlizt.creator, 'tracks': playlizt.tracks}
                playlist_dict_str = json.dumps(pl_dict)
                playlist_list_str += playlist_dict_str + '\n'
            f.write(playlist_list_str)
            
    def log_in(self):
        self.sort_users()

        username = input("Enter your username: ").strip().lower()
        user_found = False

        # Search for the user with the given username
        for user in self.users_data:
            if user.username.lower() == username:
                print(f"Welcome, {user.name}!")
                user_found = True
                self.active_user = user
                if user.type == 'musician':
                    self.current_user = False
                elif user.type == 'listener':
                    self.current_user = True
                break

        # If the user is not found, print an error message
        if not user_found:
            print("Invalid username.")
            
        return self.active_user

    def sort_users(self):
        for user in self.users_data:
            if user.type == "musician":
                self.musicians.append(user)
            elif user.type == "listener":
                self.listeners.append(user)
        self.users_data = self.musicians + self.listeners
        
    def print_albums(self):
        self.active_user = Users(id='id', name='name', email='email', username='username', type='type')
        albums = [album for album in self.albums if album.artist == self.active_user.id]
        for album in albums:
            print(album)
            
    def write_album_to_txt(self, album_str):
        with open('albums.txt', 'a', encoding='utf-8') as f:
            f.write(album_str + '\n')
            
    def write_user_to_txt(self, user_str):
        with open('users.txt', 'a', encoding='utf-8')  as f:
            f.write(user_str + '\n')
    
    def write_playlist_to_txt(self, playlist_str):
        with open('playlists.txt', 'a', encoding='utf-8') as f:
            f.write(playlist_str + '\n')
                
    def create_album(self):
        
        id= str(uuid.uuid4())
        name = input("Enter album's name: ")
        while True:
            if name == "":
                print("You should have text in your album's name")
                name = input("Enter album's name: ")
            else:
                break
        description = input("Enter album's description: ")
        while True:
            if description == "":
                print("You should have text in your album's description")
                name = input("Enter album's description: ")
            else:
                break
        cover = input("Enter url from your album's cover: ")
        while True:
            if cover == "":
                print("Invalid url")
                cover = input("Enter url from your album's cover: ")
            else:
                break
        published = str(datetime.datetime.now())

        genre = input("Enter album's genre: ")
        while True:
            if genre == "":
                print("You should have text  in your album's genre")
                genre = input("Enter album's genre: ")
            else:
                break
        
        tracklist = []
        while True: 
            print("1. Add\n2. Exit\n")
            x = int(input("Enter option: "))
            if x == 1:
                id = str(uuid.uuid4())
                name = input("Enter song's name: ")
                while True:
                    if name == "":
                        print("You should  have a valid name for the song.")
                        name = input("Enter song's name: ")
                    else:
                        break
                
                minutes = int(input("Enter minutes: "))
                while True:
                    if minutes < 0 or minutes > 59:
                        print(f"Invalid number:")
                        minutes = int(input("Enter minutes: "))
                    else:
                        break
                    
                seconds = int(input("Enter seconds: "))
                while True:
                    if seconds < 0 or seconds > 59:
                        print(f"Invalid number")
                        seconds = int(input("Enter seconds: "))
                    else:
                        break
                    
                duration = str(minutes) +":"+ str(seconds)
                        
                link = input("Enter song's url: ")
                while True:
                    if link == "":
                        print("Invalid url")
                        link = input("Enter song's url: ")
                    else:
                        break
                song = {"id": id, "name": name, "duration": duration, "link": link}     
                self.songs.append(song)
                tracklist.append(song)
                print("1. Add\n2. Finish\n")
                x = int(input('Enter option: '))
            elif x == 2:
                print(f'your album {name} has been succesfully')
                break
            else: 
                print("Invalid option. Please try again")
        album = {"id": id, "name": name, "description": description, "cover": cover, "published": published, "genre": genre, "tracklist": tracklist} 
        album_str = json.dumps(album)
        self.write_album_to_txt(album_str)
    
    def load_songs_from_albums_file(self):
        self.songs = []
        with open('albums.txt', 'r', encoding='utf-8') as f:
            for line in f:
                album = json.loads(line)
                for track_data in album['tracklist']:
                    self.songs.append(track_data)
    
    def create_playlist(self):
    
        id = str(uuid.uuid4())
        name = input("Enter playlist's name: ")
        while True:
            if name == "":
                print("Invalid name")
                name = input("Enter playlist's name: ")
            else:
                break 
        description = input("Enter the description: ")
        while True:
            if description == "":
                print("Invalid description")
                description = input("Enter the description: ")
            else:
                break
        creator = input("Enter creator's name: ")
        while True:
            if creator == "":
                print("Invalid name")
                creator = input("Enter creator's name: ")
            else:
                break
        creator_id = [user.id for user in self.users_data if user.name == creator or user.username == creator]
        if not creator_id:
            print(f'No user found with name {creator}')
            return None
        self.load_songs_from_albums_file()  # Load the songs from the albums.txt file
        song_names = [track['name'] for track in self.songs]
        tracks = []
        if not song_names:
            print('No songs found')
            return

        # Prompt the user for the name of the song
        while True:
            song_name = input('Enter the name of the song or type "done" to finish: ')
            if song_name.lower() == 'done':
                break
            if song_name in song_names:
                tracks.append(next(track['id'] for track in self.songs if track['name'] == song_name))
            else:
                print(f'No song found with name {song_name}')

        
        playlists = {"id": id, "name": name, "description": description, "creator": creator, "tracks": tracks}
        
        with open('playlists.txt', 'a', encoding='utf-8') as f:
            json_playlist = json.dumps([playlists])
            f.write(json_playlist + '\n')
            
        self.playlists.append(playlists)
        
        print(f" {name} Playlist has been succesfully created ")   
         
    def add_songs(self):
        id = str(uuid.uuid4())
        name = input("Enter song's name: ")
        while True:
            if name == "":
                print("You should  have a valid name for the song.")
                name = input("Enter song's name: ")
            else:
                break
        
        minutes = int(input("Enter minutes: "))
        while True:
            if minutes < 0 or minutes > 59:
                print(f"Invalid number:")
                minutes = int(input("Enter minutes: "))
            else:
                break
            
        seconds = int(input("Enter seconds: "))
        while True:
            if seconds < 0 or seconds > 59:
                print(f"Invalid number")
                seconds = int(input("Enter seconds: "))
            else:
                break
            
        duration = str(minutes) +":"+ str(seconds)
                
        link = input("Enter song's url: ")
        while True:
            if link == "":
                print("Invalid url")
                link = input("Enter song's url: ")
            else:
                break
        song = {"id": id, "name": name, "duration": duration, "link": link}     
        self.songs.append(song)
        return song
    
    def search(self):
        while True:
            search_query = input('Search for a user by name or username: ')
            if not search_query:
                print('Search query cannot be empty. Try again.')
                continue

            # Read the user data from the text file
            with open('users.txt', 'r', encoding='utf-8') as f:
                user_data = f.read()

            # Parse the user data from the text file
            users = [Users(**json.loads(line)) for line in user_data.strip().split('\n') if line]

            # Search for users by name or username
            search_results = [user for user in users if search_query.lower() in user.name.lower() or search_query.lower() in user.username.lower()]

            if not search_results:
                print('No users found. Try again.')
                continue

            # Print the search results
            print('\nSearch Results:')
            for user in search_results:
                print(user.__str__())

            # Ask the user if they want to view more details about a specific user
            view_details = input('\nDo you want to view more details about a user? (yes/no): ')
            if view_details.lower() == 'yes':
                # Get the index of the user to view details for
                user_index = int(input('Enter the index of the user: '))
                if 0 <= user_index < len(search_results):
                    # Print the details of the user?
                    print(search_results[user_index])
                else:
                    print('Invalid index. Try again.')
            else:
                break
        
    def change_information(self, user):
        # Mostrar las opciones de información que se pueden cambiar
        print("Account options:")
        print("1. Change username")
        print("2. Change email")
        print("3. Go back")

        # Solicitar al usuario que elija una opción
        option = int(input("Enter the number assigned to the option you want to select: "))

        # Cambiar la información del usuario según la opción elegida
        if option == 1:  # Cambiar nombre de usuario
            new_username = input("Enter new username: ")
            user.username = new_username #Para borrar datos de la cuenta, dejar el string vacio
        elif option == 2:  # Cambiar correo electrónico
            new_email = input("Enter new email: ")
            user.email = new_email
        elif option == 3:  # Volver al menú principal
            return
        else:
            print("Invalid option, please try again.")
    
    def search_songs(self):
        while True:
            search_query = input('Search for a song by name, to stop this function write "done": ').lower()
            if search_query == 'done':
                break
            elif not search_query:
                print('Search query cannot be empty. Try again.')
                continue

            search_results = [song for song in self.songs if search_query in song.name.lower()]

            if not search_results:
                print('No songs found. Try again.')
                continue

            print('\nSearch Results:')
            for idx, song in enumerate(search_results):
                print(f'{idx + 1}. {song.name}')

            break
    
    def listener_menu(self):
            # Add the new menu options for the listener
            while True:
                print('''
                    Listener Menu

                    1. View profile information
                    2. Create new playlist
                    3. Search for songs
                    4. Search for users
                    5. log out
                    6. Change information
                ''')

                option = int(input('Enter the number assigned to the option you want to select: '))

                if option == 1: 
                    print(self.active_user)
                elif option == 2: 
                    self.create_playlist()
                elif option == 3:
                    self.search_songs()
                elif option == 4:
                    self.search()
                elif option == 5:  # Log out
                    self.current_user = None
                    break
                elif option == 6:
                    self.change_information(self.active_user)
                else:
                    print("Invalid option. Please try again.")     
                       
    def musician_menu(self):
        # Add the new menu options for the musician
        while True:
            print('''
                Musician Menu

                1. View profile information
                2. Upload new albums
                3. View your albums
                4. Log out
                5. Change information
            ''')

            option = int(input('Enter the number assigned to the option you want to select: '))

            if option == 1:
                active_users_info = '\n'.join(str(user) for user in [self.active_user])
                print(active_users_info)
            elif option == 2:
                self.create_album()
            elif option == 3:
                self.print_albums()
            elif option == 4:
                self.current_user = None
                break
            elif option == 5:
                self.change_information(self.active_user)
            else:
                print("Invalid option. Please try again.")
                
    def run(self):
        while True:
            print('''\nWelcome to Metrotify. How can I help you?\n\
                   1. Log in\n\
                   2. Sign up\n\
                   3. Exit''')

            option = int(input('Enter the number assigned to the option you want to select: '))

            if option == 1:  # Log In
                if self.current_user is not None:
                    print(f'You are already logged in as {self.current_user.name}')    
                else:
                    if self.log_in():
                        if self.current_user == False:
                            self.musician_menu()
                        elif self.current_user == True:
                            self.listener_menu()

            elif option == 2:  # Sign Up
                self.sign_up()

            elif option == 3:
                print('Good bye!')
                break

            else:
                print("Invalid option. Please try again.")
                
app = App()
app.load_users()
app.load_albums()
app.load_playlist()
app.run()