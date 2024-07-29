from flask import request, jsonify
from app import app, db
from models import User

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route('/users/<account_number>', methods=['GET'])
def get_user_by_account_number(account_number):
    user = User.query.filter_by(account_number=account_number).first()
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@app.route('/users/bulk', methods=['POST'])
def bulk_upload_users():
    # Logic for bulk upload with pause and resume functionality
    pass
