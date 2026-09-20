from flask import Flask
from config import Config
from models import User, db

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

if __name__ == "__main__":
    app.run(debug=True)