from flask import Flask
from myApp import models, store, models_data

app = Flask(__name__)


member_store = store.MemberStore()
post_store = store.PostStore()

from myApp.views import *
from myApp.api import *

models_data.add_stores(post_store, member_store)
