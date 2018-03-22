from myApp import db


class Member(db.Model):
    """ Members Details Class"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    posts = db.relationship("Post", backref="members")

    def __repr__(self):
        return f'Member id : {self.id}\nMember Name : {self.name}\nMember Age : {self.age}'

    def as_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "age": self.age,
                "posts": self.posts,
                }


class Post(db.Model):
    """ Posts Details Class"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(250))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def __repr__(self):
        return f'Post id : {self.id}\nPost title : {self.title}\nPost content : {self.content}'

    def as_dict(self):
        return {
                "id": self.id,
                "title": self.title,
                "content": self.content,
                "member_id": self.member_id,
                "date": self.date,
                }

