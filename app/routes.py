from flask import jsonify, request, render_template
from app import app, mongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

@app.route('/')
def index():
    return render_template('index.html')

@app.route ("/hello/")
@app.route ("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    user_id = mongo.db.users.insert_one({'name': name, 'email': email}).inserted_id
    return jsonify(message="User added successfully!", user_id=str(user_id))

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify(list(users))
