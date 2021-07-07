import requests
import json

response = requests.get("https://api.github.com")
print(response.text)

data = response.json()
print(data)

print()

photo_response = requests.get("https://jsonplaceholder.typicode.com/photos", params=b'albumId=2')
print(photo_response.json())

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


response = requests.post("")
