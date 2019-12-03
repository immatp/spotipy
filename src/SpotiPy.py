from src.custom_exceptions.RegistrationEmailInUse import RegistrationEmailInUse
from src.custom_exceptions.InsecureRegistrationPassword import InsecureRegistrationPassword

class SpotiPy:

    def __init__(self):
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



