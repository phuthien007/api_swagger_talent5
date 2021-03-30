import connexion
import six
from sqlalchemy import and_, or_
from swagger_server.models.registrations import Registrations  # noqa: E501
from swagger_server import util
from swagger_server.controllers.users_controller import*
from swagger_server.controllers.utils import*
from swagger_server.controllers import*
@token_required
def add_registration(f,body):  # noqa: E501
    
    """add a registrations

    method to add a registration # noqa: E501

    :param body: create exam_result object
    :type body: dict | bytes

    :rtype: Registrations
    """
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body.class_id or not body.student_id:
        return jsonify({"message":"you are missing argument"}), 400
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == body.class_id.class_id, Registrations_instants.student_id == body.student_id.student_id,Registrations_instants.status == body.status, Registrations_instants.status == body.status, Registrations_instants.create_date == body.create_date  )).first()
    if item:
        return jsonify({"message":"record registration is exist"}),400
    try:
        data_class= classes_controller.get_classes_by_id(body.class_id.class_id)
        data_student = students_controller.get_student_by_id(body.student_id.student_id)
        new_registration = Registrations_instants(class_id = body.class_id.class_id, student_id = body.student_id.student_id, status= body.status, register_day= body.register_day, create_date= body.create_date)
        add_data(new_registration)
        item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == body.class_id.class_id, Registrations_instants.student_id == body.student_id.student_id,Registrations_instants.status == body.status, Registrations_instants.status == body.status, Registrations_instants.create_date == body.create_date  )).first()   
        if not item:
            return errors["400"][0],errors["400"][1] 
        data={
            "class_id": data_class,
            "create_date": item.create_date,
            "register_day": item.register_day,
            "student_id": data_student,
            "status": item.status,
        }
            # return make_response('you is missing a argument', 401, {'WWW-Authenticate':'Basic realm = "The User does not exist!"'}) 
        return data
    except Exception as e:
        return jsonify({"message":f"{e}"}),400
@token_required
def del_registration_by_id(f, class_id, student_id):  # noqa: E501
   
    """delete a registration by id

    method to delete a registration by registration_id # noqa: E501

    :param registration_id: fill in id a registration_id
    :type registration_id: int

    :rtype: None
    """
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == class_id, Registrations_instants.student_id == student_id)).first()
    if not item:
        return jsonify({"message":"registration is not exist"}),400
    delete_data(item)
    return 'success'

@token_required
def get_all_registrations(f,key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all registrations

    method to get data registrations # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Registrations]
    """
    rows= get_all_data(Registrations_instants)
    if not rows:
        return jsonify({"message":"bad request"}),400
    # if key_word:
    if key_word:
        try:
            key_word = int(key_word)
            rows= rows.filter(or_(Registrations_instants.class_id == key_word, Registrations_instants.student_id == key_word))
        except Exception as e:
            print(e)
            rows= rows.filter(Registrations_instants.status.like(f'%{key_word}%'))
    if records_per_page:
        rows = rows.limit(records_per_page)
        if page_num:
            rows= rows.offset(records_per_page * page_num)

    data=[]
    for item in rows:
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data_student = students_controller.get_student_by_id(item.student_id)
        data.append({
            "class_id": data_class,
            "create_date": item.create_date,
            "register_day": item.register_day,
            "student_id": data_student,
            "status": item.status,
        })
    return data

@token_required
def get_registration_by_id(f,class_id, student_id):  # noqa: E501
    """Show detail a registrations by id

    method to show info a registration by registration_id # noqa: E501

    :param registration_id: fill in id a registration
    :type registration_id: int

    :rtype: Registrations
    """
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == class_id, Registrations_instants.student_id == student_id)).first()
    if not item:
        return jsonify({"message":"registration is not exist"}),400
    data=[]
    data_class= classes_controller.get_classes_by_id(item.class_id)
    data_student = students_controller.get_student_by_id(item.student_id)
    data={
        "class_id": data_class,
        "create_date": item.create_date,
        "register_day": item.register_day,
        "student_id": data_student,
        "status": item.status,
    }
    return data
@token_required
def update_registration(f,body):  # noqa: E501
  
    """method to update

     # noqa: E501

    :param body: update registration object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    
    try:
        current_registration= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == body.class_id.class_id, Registrations_instants.student_id == body.student_id.student_id)).first()
        current_event.register_day= body.register_day,
        current_registration.status= body.status,
        session.commit()
        return body
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message":f"{e}"}),400
    finally:
        session.close()