
from flask import jsonify, Blueprint, request
from flask.views import MethodView
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from hello_books import app
from hello_books.api.models import HelloBooks


#instantiate blueprint and assign to var auth 
auth = Blueprint('auth', __name__)

initHelloBooks = HelloBooks()

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    sent_data = request.get_json(force = True)
    data = {
      'user_id' : len(initHelloBooks.users_list) + 1,
      'name' : sent_data['name'],
      'email' : sent_data['email'],
      'password' : sent_data['password']
    }
    #data['user_id'] = initHelloBooks.users_counter = initHelloBooks.users_counter + 1
    return initHelloBooks.user_registration(data), 201

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    sent_data = request.get_json(force = True)
    data = {
      'email' : sent_data['email'],
      'password' : sent_data['password']
    }
    return initHelloBooks.user_login(data),200

@app.route('/api/v1/auth/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({'message': 'You are now logged out'}), 200


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    return jsonify({'message': 'registered'})

@app.route('/api/v1/auth/users')
@jwt_required
def view_users():
    return initHelloBooks.view_users(), 200