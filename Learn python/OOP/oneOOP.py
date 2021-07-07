import random


class User():
    id = random.randrange(0, 999)

    def __init__ (self, login, password, name, secname = "", about = ""):
        self.login = login
        self.__password = password #Делаю атрибут "приватным/защищенным"
        self.name = name
        self.secname = secname
        self.about = about
        self.id = User.id

    def chek_log(self, sing_in):
        if not sing_in:
            return False

        else:
            for login, password in sing_in.items():
                if (login == self.login) and (password == self.__password):
                    return True

    def restorePassword(self):
        password = input("Input you new password: ")
        answer = input("You sure? y/n: ")
        answerListYes = ["y", "yes", "accept"]
        answerListNo = ["n", "no", "not", "refuse"]

        if answer in answerListYes:
            self.__password = password

            return True


    def menu(self):
            print("Меню")
            print("Выберите пункт:")
            print("1. Профиль")
            print("2. Смена пороля")

            answer = input("Введите цифры:")
            if answer == "1":
                self.profile()
            elif answer == "2":
                self.restorePassword()

    def profile(self):
            print(f"\nВаше имя: {self.name} ")
            print(f"Ваше фамилия: {self.secname} ")
            print(f"Ваше описание: {self.about} \n")

            self.menu()


    def sing_inFunc(self):
        login = input("Login: ")
        password = input("Pass: ")

        sing_in = {login : password}

        print(sing_in)
        login = sing_in
        return sing_in

i = 0
userOne = User("Kyk", "1234", "Jon")
print(f"\n {userOne.id} \n" )
login = userOne.sing_inFunc()
while True:
    if userOne.chek_log(login):
        userOne.menu()

    elif i < 3:
        login = userOne.sing_inFunc()

        if userOne.chek_log(login):

            userOne.menu()
        else:
            i+=1

    else:
        print("Вы три раза неправильно ввели логин или пороль")
        break
