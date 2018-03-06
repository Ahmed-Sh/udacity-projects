import models

dummy_members = [models.Member('ahmed', 30),
                 models.Member('Yasser', 40),
                 models.Member('Omar', 45),
                 ]

dummy_posts = [models.Post('Udacity', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.', dummy_members[0].id),
               models.Post('Flask-Project', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                                   mauris condimentum nibh, ut fermentum massa justo sit amet risus.', dummy_members[1].id),
               models.Post('1MAC Full Stack', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.', dummy_members[2].id),
               ]


def add_stores(post_store, member_store):
    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)
