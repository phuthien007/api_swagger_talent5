import connexion
import six
from swagger_server.controllers.utils import *
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.users import Users  # noqa: E501
from swagger_server import util, app
from sqlalchemy import or_
from datetime import datetime, timedelta
from flask import jsonify, make_response, request
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token= None
        if 'Authorization' in request.headers:
            token= list(request.headers['Authorization'].split())[1]
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            data= jwt.decode(token, app.secret_key)
            user= session.query(Users_instants).filter(Users_instants.user_id == data['user_id']).first()
        except Exception as e:
            
            return jsonify({'message':'Token is invalid'}),401
        return f(user, *args, **kwargs)
    return decorated
def create_user(body):  # noqa: E501
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501
    username= body.username
    email= body.email
    password= body.password
    fullname= body.fullname
    # validate username and email
    temp_user= session.query(Users_instants).filter(or_(Users_instants.username == username,Users_instants.email == email )).first()
    if temp_user:
        return jsonify({'message':'User already exists. Please Log in.'}), 202
    
    user= Users_instants(username= username, email= email, password= generate_password_hash(password), fullname= fullname)
    session.add(user)
    session.commit()
    return "success"

def del_user_by_id(user_id):  # noqa: E501
    """delete a user by id

    method to delete a user by user_id # noqa: E501

    :param user_id: fill in id a user
    :type user_id: int

    :rtype: None 
    """
    user= session.query(Users_instants).filter(Users_instants.user_id == user_id).first()
    if not user:
        return jsonify({'message':'user does not exist'}), 401
    delete_data(user)
    return "success"


def get_all_users():  # noqa: E501
    """the method to show all users

    you can show all users # noqa: E501


    :rtype: List[Users]
    """
    rows= get_all_data(Users_instants)
    data=[]
    for user in rows:
        data.append({
        'user_id':user.user_id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'birthday': user.birthday,
        'last_login_date': user.last_login_date,
        'lockout_date': user.lockout_date,
        'login_failed_count': user.login_failed_count,
        'register_date': user.register_date,
        'forgot_password_token': user.forgot_password_token
    })
    return data


def get_user_by_id(user_id):  # noqa: E501
    """Show detail a user by id

    method to show info a user by student_id # noqa: E501

    :param user_id: fill in id a student
    :type user_id: int

    :rtype: Users
    """
    user= session.query(Users_instants).filter(Users_instants.user_id == user_id).first()
    if not user:
        return jsonify({'message':'Id Unknown'}), 401
    data= {
        'user_id':user.user_id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'birthday': user.birthday,
        'last_login_date': user.last_login_date,
        'lockout_date': user.lockout_date,
        'login_failed_count': user.login_failed_count,
        'register_date': user.register_date,
        'forgot_password_token': user.forgot_password_token
    }
    return data


def login_user(body=None):  # noqa: E501
    """log user into your system

    method to login user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    
    if not body or not body.username or not body.password:
        return make_response(
            'could not verify',
            401,
            {'WWW-Authenticate':'Basic realm = "Login required"'}
        )
    user= session.query(Users_instants).filter(Users_instants.username == body.username).first()
    if not user:
        return make_response('could not verify', 401, {'WWW-Authenticate':'Basic realm = "The User does not exist!"'}) 
    if check_password_hash(user.password, body.password):
        token= jwt.encode(
            {
            'user_id': user.user_id,
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'iat': datetime.now()
        }, app.secret_key, algorithm='HS256')
        return make_response(jsonify({'token': token.decode('utf-8') }))

def logout_user():  # noqa: E501
    """log user into your system

    method to login user # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_user(body):  # noqa: E501
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501

    if not body or not body.user_id:
        return jsonify({'message':'ID Unknown'}), 401
    user= session.query(Users_instants).filter(Users_instants.user_id == body.user_id).first()
    if not user:
        return jsonify({'message':'User does not exist'}), 401
    
    user.username= body.username,
    user.email= body.email,
    user.fullname = body.fullname,
    user.birthday= body.birthday,
    session.commit()
    data= {
        'user_id':user.user_id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'birthday': user.birthday,
        'last_login_date': user.last_login_date,
        'lockout_date': user.lockout_date,
        'login_failed_count': user.login_failed_count,
        'register_date': user.register_date,
        'forgot_password_token': user.forgot_password_token
    }
    return data