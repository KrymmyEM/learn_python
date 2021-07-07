import json

class User():
    def __init__(self, id, login, name):
        self.id = id
        self.login = login
        self.name = name


Users = {
    1:{"Admin":"Admin"},
    2:{"Jorke":"Robin"},
    3:{"Hihuh":"Jordan"}
}

json_data = json.dumps(Users, indent = 2) # serialization
print(json_data)

loaded = json.loads(json_data) # deserialization
print(type(loaded))
print(loaded)

user1 = User(1, "Admin", "Admin")

json_data = json.dumps(user1.__dict__)
print(json_data)

user1 = User(**json.loads(json_data))
print(f"{user1.id} {user1.login} {user1.name}")

class Posts:

    def __init__(self, title):
        self.title = title

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

class PostsUser:
    def __init__(self, titles):
        self.titles = titles

    @classmethod
    def from_json(cls, json_data):
        posts = list(map(Posts.from_json, json_data["titles"]))
        return cls(posts)

post1 = Posts("Admin")
post2 = Posts("Jorke")
post3 = Posts("Hihuh")

postUsr = PostsUser([post1, post2, post3])
json_data = json.dumps(postUsr, default = lambda obj: obj.__dict__)
print(json_data)

decoded_post = PostsUser.from_json(json.loads(json_data))
print(decoded_post) # Вывод получаеться в режиме dict, хотя нужно было получить отдельный объект
print(decoded_post.titles)
