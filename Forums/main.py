from Forums import models, store


def create_members():
    member1 = models.Member('ahmed', 23)
    member2 = models.Member('osama', 30)
    member3 = models.Member('ahmed', 40)
    print('='*30)
    return member1, member2, member3


members_instance = create_members()
member1, member2, member3 = members_instance
member_store = store.MemberStore()


def add_members_store(members_instance, member_store):
    for member in members_instance:
        member_store.add(member)


add_members_store(members_instance, member_store)


def print_members_list(members_list):
    for member in members_list:
        print(member)


def print_all_members(member_store):
    print_members_list(member_store.get_all())


print_all_members(member_store)

def member_by_name(member1, member_store):
    member_name = member_store.get_by_name(member1.name)
    print_members_list(member_name)


# member_by_name(member1, member_store)

def member_exist(member1, member_store):
    member_exist = member_store.entity_exists(member1)
    print(member_exist)


# member_exist(member1, member_store)


def member_by_id(member3, member_store):
    member_id = member_store.get_by_id(member3.id)
    print(f'{member_id}')


# member_by_id(member3, member_store)


def member_update(member1, member_store):
    update_member = models.Member(member1.name, member1.age)
    update_member.name = 'ahmed'
    if member1 is not update_member:
        print(update_member)
        member_store.update(update_member)
        # print(member_store.get_by_id(member1.id))

# member_update(member1, member_store)


def member_delete(member1, member_store):
    try:
        member_store.delete(member1.id)
    except ValueError:
        print('Member Not Found to delete.')


# member_delete(member1, member_store)

def create_posts():
    post1 = models.Post('hello', 'hello udacity')
    post2 = models.Post('welcome', 'Welcome World')
    post3 = models.Post('Hey', 'Hello MAC')
    print('='*30)
    return post1, post2, post3


posts_instance = create_posts()
post1, post2, post3 = posts_instance
post_store = store.PostStore()


def add_posts_store(posts_instance, post_store):
    for post in posts_instance:
        post_store.add(post)


add_posts_store(posts_instance, post_store)

def print_posts_list(posts_list):
    for post in posts_list:
        print(post)


def print_all_posts(post_store):
    print_posts_list(post_store.get_all())


print_all_posts(post_store)

def post_by_title(post1, post_store):
    post_title = post_store.get_by_title(post1.title)
    print_posts_list(post_title)


# post_by_title(post1, post_store)

def post_exist(post1, post_store):
    post_exist = post_store.entity_exists(post1)
    print(post_exist)


# post_exist(post1, post_store)


def post_by_id(post3, post_store):
    post_id = post_store.get_by_id(post3.id)
    print(f'{post_id}')


# post_by_id(post3, post_store)


def post_update(post1, post_store):
    update_post = models.Post(post1.title, post1.content)
    update_post.title = 'Welcome Egypt'
    if post1 is not update_post:
        print(update_post)
        post_store.update(update_post)
        # print(post_store.get_by_id(post1.id))

# post_update(post1, post_store)


def post_delete(post1, post_store):
    try:
        post_store.delete(6)
    except ValueError:
        print('Post Not Found to delete.')


# post_delete(post1, post_store)