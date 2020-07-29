import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "task_manager"
SECRET_KEY = os.environ.get('SECRET_KEY')


@app.route("/")
def hello():
    return "hello world... again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
