from Client.user import UserProfile
from Auth.user_data import Person


class Regstry():
    """
    Класс для осуществления регистрации пользователя
    """

    def __init__(self, mail: str, password: str, name: str, age: int):
        self.mail = mail
        self.password = password
        self.name = name
        self.age = age

    def registry(self) -> bool:
        """
        Проверяем, что если такого mail нет,
        создаём нового user в базе.
        """

        p = Person(self.mail, self.password, 1)
        up = UserProfile()
        if self.mail == p.mail:
            print("Sorry, mail already exist. Try again.")
            return False
        else:
            up.name = self.name
            up.age = self.age
            up.mail = self.mail
            p.id += 1
            up.id = p.id
            p.mail = self.mail
            p.password = self.password
            return True
    