from Forums import models, store

member1 = models.Member('ahmed', 23)
member2 = models.Member('osama', 30)

post1 = models.Post('hello', 'hello udacity')
post2 = models.Post('welcome', 'Welcome World')
post3 = models.Post('welcome', 'Welcome World')

print('*' * 20)

member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)
print(member_store.get_all())


post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print(post_store.get_all())
