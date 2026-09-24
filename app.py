from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
todos_collection = db["todos"]

@app.route("/")
def index():
    return render_template("todo.html")

@app.route("/api")
def api_route():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
