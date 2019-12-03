class Song:
    def __init__(self,name,duration,artist,genre,user_owner):
        self.__name = name
        self.__duration = duration
        self.__artist = artist
        self.__genre = genre
        self.__user_owner = user_owner
        self.__scores = []

    @property
    def name(self):
        return self.__name

    @property
    def duration(self):
        return self.__duration

    @property
    def artist(self):
        return self.__artist

    @property
    def genre(self):
        return self.__genre

    @property
    def user_owner(self):
        return self.__user_owner

    def add_score(self,score):
        self.__scores.append(score)

    def average_socore(self):
        return 0 if not self.__scores else sum(self.__scores) / len(self.__scores)






