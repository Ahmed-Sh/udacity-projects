class Member:
    """ Members Details Class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = 0

    def __str__(self):
        return f'Member Name : {self.name}\nMember Age : {self.age}\nMember id : {self.id}'


class Post:
    """ Posts Details Class"""
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.id = 0

    def __str__(self):
        return f'Post title : {self.title}\nPost content : {self.content}\nPost id : {self.id}'

