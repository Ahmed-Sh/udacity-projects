import datetime


class Member:
    """ Members Details Class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []

    def __str__(self):
        return f'Member Name : {self.name}\nMember Age : {self.age}\nMember id : {self.id}'


class Post:
    """ Posts Details Class"""

    def __init__(self, title, content, member_id=0):
        self.title = title
        self.content = content
        self.id = 0
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return f'Post title : {self.title}\nPost content : {self.content}\nPost id : {self.id}\nPost Date : {self.date}'
