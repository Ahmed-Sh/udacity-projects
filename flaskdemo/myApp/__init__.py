from flask import Flask
<<<<<<< HEAD:flaskdemo/myApp/__init__.py
from flaskdemo.myApp import store, models_data
from flaskdemo.myApp import models

||||||| merged common ancestors
from myApp import models, store, models_data
=======
from flaskdemo.myApp import store, models_data
>>>>>>> 340af82552b847027ff20608532c5375a56da151:flaskdemo/myApp/__init__.py
app = Flask(__name__)


member_store = store.MemberStore()
post_store = store.PostStore()

<<<<<<< HEAD:flaskdemo/myApp/__init__.py
from flaskdemo.myApp import *
||||||| merged common ancestors
from myApp.views import *
=======
from flaskdemo.myApp.views import *
>>>>>>> 340af82552b847027ff20608532c5375a56da151:flaskdemo/myApp/__init__.py

models_data.add_stores(post_store, member_store)
