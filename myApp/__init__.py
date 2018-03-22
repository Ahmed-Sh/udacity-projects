from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
folder_path = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from myApp import models, store, models_data
member_store = store.MemberStore()
post_store = store.PostStore()
# models_data.add_stores(post_store, member_store)

from myApp import views
from myApp import api


