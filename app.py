from flask import Flask, request, jsonify, session
from config import Config
from models import User, Contract, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    return "Connected to contract_management DB!"

@app.route("/test-users")
def test_users():
    users = User.query.all()
    return {"users": [u.name for u in users]}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        session["user_id"] = user.user_id
        return jsonify({"message": "Login successful", "role": user.role}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

@app.route("/whoami")
def whoami():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"message": "Not logged in"}), 401
    user = User.query.get(user_id)
    return jsonify({"name": user.name, "role": user.role})

@app.route("/contracts")
def get_contracts():
    contracts = Contract.query.all()
    result = []
    for c in contracts:
        result.append({
            "contract_id": c.contract_id,
            "contract_name": c.contract_name,
            "vendor_name": c.vendor_name,
            "start_date": str(c.start_date) if c.start_date else None,
            "end_date": str(c.end_date) if c.end_date else None,
            "status": c.status,
            "contract_type": c.contract_type,
            "created_by": c.creator.name if c.creator else None
        })
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)