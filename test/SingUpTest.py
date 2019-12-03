import unittest
from src.User import User
from src.SpotiPy import SpotiPy
from src.custom_exceptions.RegistrationEmailInUse import RegistrationEmailInUse


class SingUpTest(unittest.TestCase):

    def setUp(self):

        self.__spotipy = SpotiPy()

        name_new_user_1 = "Pedro"
        last_name_new_user_1 = "Perez"
        email_new_user_1 = "pedro_perez@gmail.com"
        pass_new_user_1 = "pepe1234"
        self.__new_valid_user_pedro = User(name_new_user_1, last_name_new_user_1, email_new_user_1,pass_new_user_1)

        name_new_user_2 = "Juana"
        last_name_new_user_2 = "Perez"
        email_new_user_2 = "pedro_perez@gmail.com"
        pass_new_user_2 = "juani1990"
        self.__new_invalid_user_juana = User(name_new_user_2, last_name_new_user_2, email_new_user_2,pass_new_user_2)


    def test_usuario_sin_cuenta_se_registra_con_email_disponible(self):
        self.__spotipy.register_user(self.__new_valid_user_pedro)
        self.assertTrue(self.__spotipy.is_registered(self.__new_valid_user_pedro.email))

    def test_usuario_sin_cuenta_se_registra_con_email_no_disponible_lanza_excepcion(self):
        self.__spotipy.register_user(self.__new_valid_user_pedro)
        self.assertRaises(RegistrationEmailInUse,
                          lambda: self.__spotipy.register_user(self.__new_invalid_user_juana))


if __name__ == '__main__':
    unittest.main()
