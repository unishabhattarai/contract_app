from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- CONFIGURE THE DATABASE CONNECTION ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:unisha%40123@localhost:5432/contract_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DEFINE THE DATA MODEL ---
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    department = db.Column(db.String(100))
    role = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "role": self.role
        }
class Contract(db.Model):
    __tablename__ = 'contracts'
    contract_id = db.Column(db.Integer, primary_key=True)
    contract_name = db.Column(db.String(100))
    vendor_name = db.Column(db.String(100))
    contract_type = db.Column(db.String(100))
    status = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.contract_id,
            "name": self.contract_name,
            "vendor": self.vendor_name,
            "type": self.contract_type,
            "status": self.status
        }
# --- CREATE API ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/api/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    return jsonify([contract.to_dict() for contract in contracts])

if __name__ == '__main__':
    app.run(debug=True)