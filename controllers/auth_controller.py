from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

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


@auth_bp.route('/login', methods=['POST'])
def auth_login():
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401

@auth_bp.route('/<int:user_id>/', methods=['DELETE'])
@jwt_required()
def delete_one_user(user_id):
    authorize()

    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.first_name}' deleted successfully"}
    else:
        return {'error': f'User not found with User ID {user_id}'}, 404

def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)