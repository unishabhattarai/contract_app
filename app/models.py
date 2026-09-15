from .extensions import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "role": self.role,
        }


class Contract(db.Model):
    __tablename__ = "contracts"

    contract_id = db.Column(db.Integer, primary_key=True)
    contract_name = db.Column(db.String(100), nullable=False)
    vendor_name = db.Column(db.String(100), nullable=False)
    contract_type = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "id": self.contract_id,
            "name": self.contract_name,
            "vendor": self.vendor_name,
            "type": self.contract_type,
            "status": self.status,
        }
