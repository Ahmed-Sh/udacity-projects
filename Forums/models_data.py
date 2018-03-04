from Forums import models
from Forums import store

post_store = store.PostStore()
post_store.add(models.Post('Udacity', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))
post_store.add(models.Post('Flask-Project', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))
post_store.add(models.Post('1MAC Full Stack', 'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor \
                    mauris condimentum nibh, ut fermentum massa justo sit amet risus.'))