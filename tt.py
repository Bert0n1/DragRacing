
import hashlib


class BancAccount():
    def __init__(self, login, password):
        self.__login = login

        self.__cash = 0
        self.__is_authenticate: bool = False
        self.__password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha1(str(password).encode()).hexdigest()
        
    def autheticate(self, login, password):
        if login == self.__login:
            if self.hash_password(password) == self.__password:
                self.__is_authenticate = True
            else:
                raise Exception("Неверный пароль")
        else:
            raise Exception("Неверный логин")
        
    def add_money(self, money):
        if self.__is_authenticate:
            self.__cash += money
        else:
            raise Exception("Авторизуйтесь в системе")
        
    def get_money(self, money):
        if self.__is_authenticate:
            if self.__cash >= money:
                self.__cash -= money
        else:
            raise Exception("Авторизуйтесь в системе")

    def read_money(self):
        if self.__is_authenticate:
            return self.__cash




b = BancAccount("alex", "1234")
b.autheticate("alex", "1234")
b.hash_password("2312312")
b.add_money(1000)





