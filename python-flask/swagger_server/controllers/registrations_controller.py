import connexion
import six
from sqlalchemy import and_, or_

from swagger_server.controllers import classes_controller, students_controller
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
    if check_authorization(f,"can_add_registration") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400 
    
   
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body._class or not body.student:
        return jsonify({"message":"you are missing argument"}), 400
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == body._class.id, Registrations_instants.student_id == body.student.id,Registrations_instants.status == body.status, Registrations_instants.status == body.status, Registrations_instants.create_date == body.create_date  )).first()
    if item:
        return jsonify({"message":"record registration is exist"}),400
    try:
        data_class= classes_controller.get_classes_by_id(body._class.id)
        data_student = students_controller.get_student_by_id(body.student.id)
        new_registration = Registrations_instants(class_id = body._class.id, student_id = body.student.id, status= body.status, register_day= body.register_day, create_date= body.create_date)
        add_data(new_registration)
        item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == body._class.id, Registrations_instants.student_id == body.student.id,Registrations_instants.status == body.status, Registrations_instants.status == body.status, Registrations_instants.create_date == body.create_date  )).first()
        data=""

            # return make_response('you is missing a argument', 401, {'WWW-Authenticate':'Basic realm = "The User does not exist!"'}) 
        return get_registration_by_id(item.class_id, item.student_id)
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message":f"{e}"}),400

@token_required
def del_registration_by_id(f, class_id, student_id):  # noqa: E501
   
    """delete a registration by id

    method to delete a registration by registration_id # noqa: E501

    :param registration_id: fill in id a registration_id
    :type registration_id: int

    :rtype: None
    """
    if check_authorization(f,"can_delete_registration_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400 
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == class_id, Registrations_instants.student_id == student_id)).first()
    if not item:
        return jsonify({"message":"registration is not exist"}),400
    delete_data(item)
    return 'success'

@token_required
def get_all_registrations(f,key_word=None, page_num=0, records_per_page=20):  # noqa: E501
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
    if check_authorization(f,"can_view_all_registrations") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    rows, number_of_records= get_all_data(Registrations_instants)
    if not rows:
        return jsonify({"message":"bad request"}),400
    # if key_word:
    if key_word:
        try:
            key_word = int(key_word)
            rows= rows.filter(or_(Registrations_instants.class_id == key_word, Registrations_instants.student_id == key_word))
        except Exception as e:
            
            rows= rows.filter(Registrations_instants.status.like(f'%{key_word}%'))
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
    for item in rows:
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data_student = students_controller.get_student_by_id(item.student_id)
        data.append({
            "class": data_class,
            "create_date": item.create_date,
            "register_day": item.register_day,
            "student": data_student,
            "status": item.status,
        })
    return data,200,{"total_of_records":number_of_records,"total_of_pages": total_pages}

@token_required
def get_registration_by_id(f,class_id, student_id):  # noqa: E501
    """Show detail a registrations by id

    method to show info a registration by registration_id # noqa: E501

    :param registration_id: fill in id a registration
    :type registration_id: int

    :rtype: Registrations
    """
    if check_authorization(f,"can_view_registration_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    item= session.query(Registrations_instants).filter(and_(Registrations_instants.class_id == class_id, Registrations_instants.student_id == student_id)).first()
    if not item:
        return jsonify({"message":"registration is not exist"}),400
    data=[]
    data_class= classes_controller.get_classes_by_id(item.class_id)
    data_student = students_controller.get_student_by_id(item.student_id)
    data={
        "class": data_class,
        "create_date": item.create_date,
        "register_day": item.register_day,
        "student": data_student,
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
    if check_authorization(f,"can_update_registration") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        current_registration= get_registration_by_id(body._class.id, body.student.id)
        print(current_registration)
        current_registration['status']= body.status
        current_registration['register_day']= body.register_day
        session.commit()
        return body
    except Exception as e:
        session.rollback()
        return jsonify({"message":f"{e}"}),400
    finally:
        session.close()