from Forums import models, store

member1 = models.Member('ahmed', 23)
member2 = models.Member('osama', 30)

post1 = models.Post('hello', 'hello udacity')
post2 = models.Post('welcome', 'Welcome World')
post3 = models.Post('welcome', 'Welcome World')

print('='*30)

member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)

print(member_store.get_all())

member_exist = member_store.entity_exists(member1)
print(member_exist)

member_id = member_store.get_by_id(member2.id)
print(f'Member Name : {member_id.name}')

member_del = member_store.delete(member1.id)
print(member_del)


post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print(post_store.get_all())

post_exist = post_store.entity_exists(post1)
print(post_exist)

post_id = post_store.get_by_id(post2.id)
print(f'Post title : {post_id.title}')

post_delete = post_store.delete(post1.id)
print(post_delete)