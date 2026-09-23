from app import app
from models import db, User

# Map each user's email to the password you want to set for them
passwords = {
    "anjelinadong@bank.rp": "changeme123",
    "unishabhattarai@bank.rp": "changeme123",
    "lilysingh@bank.rp": "changeme123",
    "minalama@bank.rp": "changeme123",
    "bibekthapa@bank.rp": "changeme123",
}

with app.app_context():
    for email, pwd in passwords.items():
        user = User.query.filter_by(email=email).first()
        if user:
            user.set_password(pwd)
            print(f"Password set for {user.name} ({email})")
        else:
            print(f"No user found with email {email}")
    db.session.commit()
    print("Done.")