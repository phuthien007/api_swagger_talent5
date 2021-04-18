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
    def decorated(*args,**kwargs):
        token= None
        if 'Authorization' in request.headers:
            token= list(request.headers.get('Authorization').split())[1]
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data= jwt.decode(token,app.secret_key, algorithms='HS256')
            user= session.query(Users_instants).filter(Users_instants.id == data.get('id')).first()
        except Exception as e:
            return jsonify({'message':'Token is invalid'}),401
        return f(user, *args, **kwargs)
    return decorated
def check_authorization(user,permistion):
    try:
        permis= get_per_id(permistion)
        check1 = get_permis_each_role(role=user.role,per_id= permis)
        check2 = get_permis_each_author(user_id=user.id, per_id=permis)
        if check1 == None and  check2 == None:
            return False
        return True 
    except Exception as e:
        return False
def create_user(body):  # noqa: E501
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        username= body.username
        email= body.email
        password= body.password
        fullname= body.fullname
        # validate username and email
        temp_user= session.query(Users_instants).filter(or_(Users_instants.username == username,Users_instants.email == email )).first()
        if temp_user:
            return jsonify({'message':'User already exists. Please Log in.'}), 202
        
        user= Users_instants(username= username, email= email, password= generate_password_hash(password), fullname= fullname, role="user")
        session.add(user)
        session.commit()
        temp_user= session.query(Users_instants).filter(or_(Users_instants.username == username,Users_instants.email == email )).first()        
        return get_user_by_id(temp_user.id)
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message":"A error in process"}), 400
@token_required
def del_user_by_id(f,user_id):  # noqa: E501
    """delete a user by id

    method to delete a user by user_id # noqa: E501

    :param user_id: fill in id a user
    :type user_id: int

    :rtype: None 
    """
    if check_authorization(f,permistion="can_delete_user_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    user= session.query(Users_instants).filter(Users_instants.id == user_id).first()
    if not user:
        return jsonify({'message':'user does not exist'}), 401
    delete_data(user)
    return "success"


@token_required
def get_all_users(f,key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """the method to show all users

    you can show all users # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Users]
    """
    
    if check_authorization(f,permistion="can_view_all_users") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    rows,number_of_records= get_all_data(Users_instants)
    if rows == None:
        return errors["400"][0],errors["400"][1]
    if key_word:
        rows= rows.filter(or_(Users_instants.email.like(f'%{key_word}%'),Users_instants.fullname.like(f'%{key_word}%'),Users_instants.username.like(f'%{key_word}%')))
    total_pages= number_of_records//20 + 1
    records_per_page = 0 if records_per_page <0 else records_per_page
    if records_per_page>=0:
        if page_num>=0:
            rows= rows.offset(records_per_page* page_num)
            if number_of_records > records_per_page and int(records_per_page) != 20:
                number_of_records = int(records_per_page)
            total_pages= number_of_records//20 + 1
            if records_per_page > 20:
                records_per_page = 20
            rows= rows.limit(records_per_page)
    data=[]
    for user in rows:
        data.append({
        'id':user.id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'birthday': user.birthday,
        'last_login_date': user.last_login_date,
        'lockout_date': user.lockout_date,
        'login_failed_count': user.login_failed_count,
        'register_date': user.register_date,
        'forgot_password_token': user.forgot_password_token,
        'role':user.role
    })
    return data,200,{"total_of_records":number_of_records,"total_of_pages": total_pages}
    


@token_required
def get_user_by_id(f,user_id):  # noqa: E501
    """Show detail a user by id

    method to show info a user by student_id # noqa: E501

    :param user_id: fill in id a student
    :type user_id: int

    :rtype: Users
    """
    
    if check_authorization(f,permistion="can_view_user_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    get_user= session.query(Users_instants).filter(Users_instants.id == user_id).first()
    if not get_user:
        return jsonify({'message':'Id Unknown'}), 401
    data= {
        'id':get_user.id,
        'username': get_user.username,
        'email': get_user.email,
        'fullname': get_user.fullname,
        'birthday': get_user.birthday,
        'last_login_date': get_user.last_login_date,
        'lockout_date': get_user.lockout_date,
        'login_failed_count': get_user.login_failed_count,
        'register_date': get_user.register_date,
        'forgot_password_token': get_user.forgot_password_token,
        'role':get_user.role
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
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'iat': datetime.utcnow()
        }, app.secret_key, algorithm='HS256')
        return make_response(jsonify({'token': token }))

@token_required
def update_user(f,body):  # noqa: E501
    
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    
    if check_authorization(f,permistion="can_update_user") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body.id:
        return jsonify({'message':'ID Unknown'}), 401
    user= session.query(Users_instants).filter(Users_instants.id == body.id).first()
    if not user:
        return jsonify({'message':'User does not exist'}), 401
    
    user.username= body.username,
    user.email= body.email,
    user.fullname = body.fullname,
    user.birthday= body.birthday,
    session.commit()
    data= {
        'id':user.id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'birthday': user.birthday,
        'last_login_date': user.last_login_date,
        'lockout_date': user.lockout_date,
        'login_failed_count': user.login_failed_count,
        'register_date': user.register_date,
        'forgot_password_token': user.forgot_password_token,
        'role':user.role
    }
    return data