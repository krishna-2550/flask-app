from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------- HARD CODED USER (LOGIN) ----------------
USER = {
    "email": "admin@gmail.com",
    "password": "1234"
}

# ---------------- TEMP DATABASE ----------------
users = [
    {"id": 1, "name": "Krishna"},
    {"id": 2, "name": "Rahul"}
]

# ---------------- HOME (LOGIN FORM - GET) ----------------
@app.route("/")
def home():
    return '''
        <h2>Login</h2>
        <form action="/login">
            Email: <input name="email"><br><br>
            Password: <input name="password"><br><br>
            <button>Login</button>
        </form>
    '''

# ---------------- LOGIN CHECK ----------------
@app.route("/login")
def login():
    email = request.args.get("email")
    password = request.args.get("password")

    if email == USER["email"] and password == USER["password"]:
        return "Login Successful ✅"
    else:
        return "Invalid Credentials ❌"


# ================== API PART ==================

# ---------------- GET USERS ----------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# ---------------- ADD USER ----------------
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added", "users": users})

# ---------------- UPDATE USER ----------------
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    for user in users:
        if user["id"] == id:
            user["name"] = data.get("name", user["name"])
            return jsonify({"message": "User updated", "user": user})

    return jsonify({"error": "User not found"})

# ---------------- DELETE USER ----------------
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify({"message": "User deleted", "users": users})

    return jsonify({"error": "User not found"})


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)