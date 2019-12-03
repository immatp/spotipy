class User(object):

    def __init__(self, name, last_name, email,password):
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    def is_valid_password(self, password):
        return self.__password == password
