import unittest
from src.User import User
from src.SpotiPy import SpotiPy
from src.Genres import GENRES
from src.Song import Song
from src.custom_exceptions.DuplicatedSong import DuplicatedSong

class UserSongsTestCase(unittest.TestCase):
    def setUp(self):

        self.__spotipy = SpotiPy()
        name_new_user = "Carla"
        last_name_new_user = "Lopez"
        email_new_user = "carla_lopez@gmail.com"
        self._pass_new_user = "car1234.+-p"
        self.__user_carla = User(name_new_user,
                                 last_name_new_user,
                                 email_new_user,
                                 self._pass_new_user)
        self.__spotipy.register_user(self.__user_carla)

        name_new_user_1 = "Pedro"
        last_name_new_user_1 = "Perez"
        email_new_user_1 = "pedro_perez@gmail.com"
        pass_new_user_1 = "pepe1234__"
        self.__user_pedro = User(name_new_user_1, last_name_new_user_1, email_new_user_1, pass_new_user_1)
        self.__spotipy.register_user(self.__user_pedro)



        self.__despacito = Song("despacito",3.0,"Luis Fonsi",GENRES.POP,self.__user_carla)
        self.__spotipy.add_song(self.__despacito)


    def test_usuario_con_cuenta_sube_tema_desapacito(self):
        expectedDespacito = self.__spotipy.get_song_by_name(self.__despacito.name)
        self.assertEqual(expectedDespacito,self.__despacito)

    def test_usuario_con_cuenta_sube_tema_duplicado_lanza_excepcion(self):
        despacito_repetido = self.__despacito
        self.assertRaises(DuplicatedSong, lambda: self.__spotipy.add_song(despacito_repetido))

    def test_usuario_con_cuenta_elimina_su_tema_despacito(self):
        expectedDespacito = self.__spotipy.get_song_by_name(self.__despacito.name)
        self.assertEqual(expectedDespacito,self.__despacito)

        self.__spotipy.delete_song_of_user(self.__despacito, self.__user_carla)
        expectedNonExistSong = self.__spotipy.get_song_by_name(self.__despacito.name)
        self.assertIsNone(expectedNonExistSong)

    def test_usuario_con_cuenta_puntua_despacito(self):
        self.__spotipy.rate_song_by_user(self.__despacito,10)
        self.__spotipy.rate_song_by_user(self.__despacito, 5)

        current_average_rate = self.__spotipy.get_song_average_rate(self.__despacito)
        expected_average_rate = 7.5

        self.assertEqual(current_average_rate,expected_average_rate)


if __name__ == '__main__':
    unittest.main()
