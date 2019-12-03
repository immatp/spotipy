from src.custom_exceptions.RegistrationEmailInUse import RegistrationEmailInUse


class SpotiPy:

    def __init__(self):
        self.__users = []

    def register_user(self, new_user):
        if self.__is_available_email(new_user.email):
            self.__users.append(new_user)
        else:
            raise RegistrationEmailInUse(new_user.email)

    def __is_available_email(self, email):
        return email not in map(lambda u: u.email, self.__users)

    def is_registered(self,email):
        return not self.__is_available_email(email)
