import unittest
from src.User import User
from src.SpotiPy import SpotiPy


class LoginTestCase(unittest.TestCase):

    def setUp(self):

        self.__spotipy = SpotiPy()
        name_new_user = "Carla"
        last_name_new_user = "Lopez"
        email_new_user = "carla_lopez@gmail.com"
        self._pass_new_user = "car1234"
        self.__user_carla = User(name_new_user,
                                 last_name_new_user,
                                 email_new_user,
                                 self._pass_new_user)
        self.__spotipy.register_user(self.__user_carla)



    def test_usuario_registrato_se_puede_loguear(self):
        self.assertTrue(self.__spotipy.is_valid_login(self.__user_carla.email,
                                                      self._pass_new_user))

    def test_usuario_registrato_con_credenciales_invalidas_no_se_puede_loguear(self):
        self.assertFalse(self.__spotipy.is_valid_login(self.__user_carla.email,
                                                      "no es valida"))

    def test_usuario_no_registrado_no_se_puede_loguear(self):
        self.assertFalse(self.__spotipy.is_valid_login("emailnoexiste@gmail.com",
                                                       "car1234"))


if __name__ == '__main__':
    unittest.main()
