from myApp import models, db

dummy_members = [
                models.Member(name='ahmed', age=30),
                models.Member(name='Yasser', age=40),
                models.Member(name='Omar', age=45),
                ]

dummy_posts = [
                models.Post(title='Udacity', content='Donec id elit non mi or \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.', member_id=0),
                models.Post(title='Flask-Project', content='Donec id elit non mac cursus commodo, tortor \
                                   mauris condimentum nibh, ut fermentum massa justo sit amet risus.', member_id=1),
                models.Post(title='1MAC Full Stack', content='Donec id elit non mi lus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.', member_id=0),
                models.Post(title="Architecture", content="Spectacular art", member_id=2),
                models.Post(title="Astronomy", content="Space is awesome", member_id=2),

                models.Post(title="Geology", content="Earth is our friend", member_id=3),
                models.Post(title="ComputerSci", content="Our passion", member_id=3),
                models.Post(title="Algorithms", content="Yeah, more of that", member_id=3),
                models.Post(title="Operating Systems", content="Ewww", member_id=3),
               ]


def add_stores(member_store, post_store):
    db.drop_all()
    db.create_all()

    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)
