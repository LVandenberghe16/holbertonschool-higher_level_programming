#!/usr/bin/python3
"""
Module for fetching and saving posts from a RESTful API.
"""


from flask import Flask, jsonify, request


app = Flask(__name__)

users = {"jane": {"name": "John", "age": 28, "city": "Los Angeles"}}

@app.route('/')
def home():
    return "testing flask"

@app.route('/data')
def data():
    return jsonify(users)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def show_user_profile(username):
    return users.get(username, "User not found")

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "username" not in data or "name" not in data:
        return jsonify({"error": "Invalid data, 'username' and 'name'"}), 400
    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    users[username] = {
        "name": data["name"],
        "age": data.get("age", "Not specified"),
        "city": data.get("city", "Unknown")
    }
    return jsonify({"message": "User added successfully",
                    "user": users[username]}), 201


if __name__ == '__main__':
    app.run()