import random

class Post:
    id = random.randrange(0, 999)
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

    def display(self):
        return f"{self.title} \n {self.text} \n {self.date} \n"

    @classmethod
    def postConstruct_c(cls, title, text):
        return cls(title, text, "01.01.2020")

    @staticmethod
    def postConstruct_s(title, text):
        return Post(title, text, "01.01.2020")

onePost = Post("One post in init", "Text one post in init", "01.01.2020")
print(onePost.display())

onePost_c = Post.postConstruct_c("One post in class method", "Text one post class method")
print(onePost_c.display())

onePost_s = Post.postConstruct_s("One post in static method", "Text one post static method")
print(onePost_s.display())


class OneToTwo():

    @staticmethod
    def oneToTwo(a):
        if a == 1:
            return 2

        elif a == 2:
            return 2

        else:
            return "I NEED 1 OR 2"

    @staticmethod
    def twoToOne(a):
        if a == 2:
            return 1

        elif a == 1:
            return 1

        else:
            return "I NEED 1 OR 2"


print(OneToTwo.oneToTwo(1))
print(OneToTwo.twoToOne(2))
print()
print(OneToTwo.oneToTwo(3))
print(OneToTwo.twoToOne(1))
