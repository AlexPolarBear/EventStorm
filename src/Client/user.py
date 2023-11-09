class UserProfile():
    """
    Class builder for create a user profile.
    With changes and gets information
    """

    def __init__(self, name = "Jhon", age = 23, mail = "exampl@mail.com", id = 0):
        self.name = name
        self.age = age
        self.mail = mail
        self.id = id

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age

    def set_mail(self, mail: int) -> None:
        self.mail = mail

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    