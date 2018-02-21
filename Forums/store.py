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

    def entity_exists(self, member):
        return self.get_by_id(member.id) is not None

    def delete(self, id):
        entity = self.get_by_id(id)
        if entity is not None:
            MemberStore.members.remove(entity)


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

    def entity_exists(self, post):
        return self.get_by_id(post.id) is not None

    def delete(self, id):
        entity = self.get_by_id(id)
        if entity is not None:
            PostStore.posts.remove(entity)

