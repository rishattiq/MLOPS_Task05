

from flask import Flask, request, jsonify

from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)




app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://rishattiq:Billo1234@cluster0.scnrcle.mongodb.net/"
mongo = PyMongo(app)


# Endpoint to store user information
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.json

    name = data.get('name')
    email = data.get('email')

    # Insert user data into MongoDB
    user_data = {'name': name, 'email': email}
    collection.insert_one(user_data)

    return jsonify({'message': 'User information stored successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
