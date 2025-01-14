from flask import Flask
from flask import jsonify

users = {
    "1":{'id':1,"name":"John"},
    "2":{'id':2,"name":"Aviran"}
    }


app = Flask("Aviran")

@app.route("/users")
def get_all_users():
    temp = list(users.values())
    return jsonify(temp)


@app.route("/users/<userid>")
def get_a_single_user(userid):
    SpecificUser = users[userid]
    return jsonify(SpecificUser)


app.run(host="0.0.0.0")