from flask import Flask
from flaskdemo.myApp import store, models_data
app = Flask(__name__)


member_store = store.MemberStore()
post_store = store.PostStore()

from flaskdemo.myApp.views import *

models_data.add_stores(post_store, member_store)
