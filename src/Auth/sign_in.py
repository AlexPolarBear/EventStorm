from Auth.user_data import Person

class SignIn():
    """
    Класс для осуществления входа пользователя.
    В реальности лучше так не делать.
    """

    def __init__(self, mail: str, password: str):
        self.mail = mail
        self.password = password

    def sign_in(self):
        """
        Просто проверяем, как будто бы из базы Person.
        Что если такая запись существует и равна введённым данным,
        то возвращаем id пользователя.
        В реальности, можно было бы передавать токен.
        """
        
        p = Person(self.mail, self.password, 1)
        if p.mail == self.mail:
            if p.password == self.password:
                print("Sign in successfuly!")
                return id
            else:
                print("Password is wrong. Try again.")
        else:
            print("Data is wrong...")
    