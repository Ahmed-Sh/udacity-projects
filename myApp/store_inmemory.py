import itertools
import copy


class BaseStore:

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, entity):
        entity.id = self._last_id
        self._data_provider.append(entity)
        self._last_id += 1

    def get_by_id(self, id):
        result = None
        entities = self.get_all()
        for entity in entities:
            if entity.id == id:
                result = entity
                break
        return result

    def get_by_name(self, name):
        return [entity for entity in self.get_all() if entity.name == name]

    def get_by_title(self, title):
        result = []
        all_posts = self.get_all()
        for post in all_posts:
            if post.title == title:
                result.append(post)
        return result

    def entity_exists(self, entity):
        return self.get_by_id(entity.id) is not None

    def update(self, entity):
        update_entity = self.get_all()
        result = entity
        for i, current_entity in enumerate(update_entity):
            if current_entity.id == entity.id:
                update_entity[i] = entity
        return result


    def delete(self, id):
        entity = self.get_by_id(id)
        self._data_provider.remove(entity)


class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

    # def get_all(self):
    #     return MemberStore.members
    #
    # def add(self, member):
    #     member.id = MemberStore.last_id
    #     MemberStore.members.append(member)
    #     MemberStore.last_id += 1

    # def get_by_id(self, id):
    #     result = None
    #     all_members = self.get_all()
    #     for member in all_members:
    #         if member.id == id:
    #             result = member
    #             break
    #     return result

    # def get_by_name(self, name):
    # result = []
    # all_members = self.get_all()
    # for member in all_members:
    #     if member.name == name:
    #         result.append(member)
    # return result
    # return [member for member in self.get_all() if member.name == name] # List Comprehension
    # return (member for member in self.get_all() if member.name == name)   # generator Expression

    # def entity_exists(self, member):
    #     return self.get_by_id(member.id) is not None

    # def update(self, member):
    #     update_member = self.get_all()
    #     i = 0
    #     for x in update_member:
    #         if member.id == x.id:
    #             update_member[i] = member
    #             break
    #         i += 1
    #
    # def delete(self, id):
    #     member = self.get_by_id(id)
    #     MemberStore.members.remove(member)

    def get_all_members_posts(self, all_posts):
        members_with_posts = copy.deepcopy(self.get_all())
        for member, post in itertools.product(members_with_posts, all_posts):
            if post.member_id == member.id:
                member.posts.append(post)
        return members_with_posts

    def get_top_2members(self, all_posts):
        top_posts = list(self.get_all_members_posts(all_posts))
        top_posts.sort(key=lambda post: len(post.posts), reverse=True)
        for top in range(0, 2):
            yield top_posts[top]


class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)

    # def get_all(self):
    #     return PostStore.posts
    #
    # def add(self, post):
    #     post.id = PostStore.last_id
    #     PostStore.posts.append(post)
    #     PostStore.last_id += 1
    #
    # def get_by_id(self, id):
    #     result = None
    #     all_posts = self.get_all()
    #     for post in all_posts:
    #         if post.id == id:
    #             result = post
    #             break
    #     return result
    #
    # def get_by_title(self, title):
    #     result = []
    #     all_posts = self.get_all()
    #     for post in all_posts:
    #         if post.title == title:
    #             result.append(post)
    #     return result
    #
    # def entity_exists(self, post):
    #     return self.get_by_id(post.id) is not None
    #
    # def update(self, post):
    #     update_post = self.get_all()
    #     result = post
    #     for i, current_post in enumerate(update_post):
    #         if current_post.id == post.id:
    #             update_post[i] = post
    #     return result
    #
    # def delete(self, id):
    #     post = self.get_by_id(id)
    #     PostStore.posts.remove(post)

    def get_posts_by_date(self):
        posts_by_date = copy.deepcopy(self.get_all())
        posts_by_date.sort(key=lambda post: post.date, reverse=True)
        return posts_by_date

