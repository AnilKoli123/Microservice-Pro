from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Anil", "email": "anil@example.com"},
    2: {"id": 2, "name": "Kiran", "email": "kiran@example.com"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/")
def home():
    return "User Service is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
