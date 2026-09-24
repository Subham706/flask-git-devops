@"
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

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Missing required fields"}), 400

    todo_doc = {
        "itemName": item_name,
        "itemDescription": item_description
    }
    result = todos_collection.insert_one(todo_doc)
    return jsonify({"status": "Item inserted", "id": str(result.inserted_id)}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
"@ | Out-File -FilePath app.py -Encoding utf8