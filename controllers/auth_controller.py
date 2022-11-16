from flask import Blueprint, jsonify, request
from init import db, bcrypt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError


auth_bp = Blueprint('auth', __name__, url_prefix='/auth' )

@auth_bp.route('/users/')
def get_users():
    # get info of all users
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    # create a new user
    try:
        user = User(
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            first_name = request.json.get('first_name'),
            last_name = request.json.get('last_name')
            
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409