from src.custom_exceptions.RegistrationEmailInUse import RegistrationEmailInUse
from src.custom_exceptions.InsecureRegistrationPassword import InsecureRegistrationPassword
from src.custom_exceptions.DuplicatedSong import DuplicatedSong
from src.custom_exceptions.NotAllowedUserForDeleteSong import NotAllowedUserForDeleteSong

class SpotiPy:

    def __init__(self):
        self.__songs = []
        self.__users = []

    def register_user(self, new_user):
        if self.__is_available_email(new_user.email):
            if new_user.has_secure_password():
                self.__users.append(new_user)
            else:
                raise InsecureRegistrationPassword()
        else:
            raise RegistrationEmailInUse(new_user.email)

    def __is_available_email(self, email):
        return email not in map(lambda u: u.email, self.__users)

    def is_registered(self,email):
        return not self.__is_available_email(email)

    def is_valid_login(self, email, password):
        user = self.__get_user_by_email(email)
        return user and user.is_valid_password(password)

    def __get_user_by_email(self, email):
        if not self.is_registered(email):
            return None
        else:
            return list(filter(lambda u: u.email == email, self.__users))[0]

    def add_song(self, song):
        if song.name not in map(lambda s: s.name,self.__songs):
            self.__songs.append(song)
        else:
            raise DuplicatedSong(song.name)

    def get_song_by_name(self, name):
        found = list(filter(lambda song: song.name == name,self.__songs))
        return found[0] if len(found) == 1 else None

    def delete_song_of_user(self, despacito, user_deleter):
        if despacito.user_owner != user_deleter:
            raise NotAllowedUserForDeleteSong(f"{user_deleter.name} can not delete {despacito.name}")
        self.__delete_song(despacito)

    def __delete_song(self, despacito):
        self.__songs = list(filter(lambda s: s != despacito, self.__songs))

    def rate_song_by_user(self, song, score):
        self.get_song_by_name(song.name).add_score(score)

    def get_song_average_rate(self, song):
        return self.get_song_by_name(song.name).average_socore()
