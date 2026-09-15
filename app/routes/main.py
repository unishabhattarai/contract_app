from flask import Blueprint, jsonify, render_template

from app.models import Contract, User

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/login")
def login():
    return render_template("login.html")


@main_bp.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@main_bp.route("/api/contracts", methods=["GET"])
def get_contracts():
    contracts = Contract.query.all()
    return jsonify([contract.to_dict() for contract in contracts])
