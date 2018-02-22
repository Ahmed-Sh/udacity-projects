import itertools
class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        result = None
        all_members = self.get_all()
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def get_by_name(self, name):
        # result = []
        # all_members = self.get_all()
        # for member in all_members:
        #     if member.name == name:
        #         result.append(member)
        # return result
        # return [member for member in self.get_all() if member.name == name] # List Comprehension
        return (member for member in self.get_all() if member.name == name)   # generator Expression

    def entity_exists(self, member):
        return self.get_by_id(member.id) is not None


    def update(self, member):
        update_member = self.get_all()
        i = 0
        for x in update_member:
            if member.id == x.id:
                update_member[i] = member
                break
            i += 1

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def get_all_members_posts(self, all_posts):
        all_members = self.get_all()
        for member, post in zip(all_members, all_posts):
            if post.member_id == member.id:
                member.posts.append(post)
        return all_members


class PostStore:

    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self, id):
        result = None
        all_posts = self.get_all()
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def get_by_title(self, title):
        result = []
        all_posts = self.get_all()
        for post in all_posts:
            if post.title == title:
                result.append(post)
        return result

    def entity_exists(self, post):
        return self.get_by_id(post.id) is not None

    def update(self, post):
        update_post = self.get_all()
        result = post
        for i, current_post in enumerate(update_post):
            if current_post.id == post.id:
                update_post[i] = post
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

