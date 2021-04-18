import connexion
import six

from swagger_server.models.students import Students  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

from swagger_server.controllers.users_controller import*
from sqlalchemy import or_,and_
from datetime import timezone

@token_required
def add_student(f,body):  # noqa: E501

    """add a student

    method to add a student # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Students
    """
    if check_authorization(f,"can_add_student") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = Students.from_dict(connexion.request.get_json())  # noqa: E501
    #create a new instant student
    try:
        item= session.query(Students_instants).filter(and_(Students_instants.address==body.address,Students_instants.birthday==body.birthday,Students_instants.email==body.email,Students_instants.facebook==body.facebook,Students_instants.full_name==body.full_name,Students_instants.note==body.note,Students_instants.phone==body.phone)).first()
        if item:
            return jsonify({"message":"the student is exist"}), 400
        new_student = Students_instants(address=body.address,birthday=body.birthday,email=body.email,facebook=body.facebook,full_name=body.full_name,note=body.note,phone=body.phone)
        # use func add_data is defined by utils.py
        add_data(new_student)
        item= session.query(Students_instants).filter(and_(Students_instants.address==body.address,Students_instants.birthday==body.birthday,Students_instants.email==body.email,Students_instants.facebook==body.facebook,Students_instants.full_name==body.full_name,Students_instants.note==body.note,Students_instants.phone==body.phone)).first()
        data= {
                "address": item.address,
                "birthday": item.birthday,
                "create_date": item.create_date,
                "email": item.email,
                "facebook": item.facebook,
                "full_name": item.full_name,
                "note": item.note,
                "phone": item.phone,
                "id": item.id
            }
        return data
    except Exception:
        return errors["400"][0],errors["400"][1]

@token_required
def del_student_by_id(f,student_id):  # noqa: E501
    """delete a student by id

    method to delete a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: None
    """
    if check_authorization(f,"can_delete_student_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    try:
        current_student= session.query(Students_instants).filter(Students_instants.id == student_id).first()
        current_exam_results= session.query(Exam_results_instants).filter(Exam_results_instants.student_id == current_student.id).first()
        current_registration= session.query(Registrations_instants).filter(Registrations_instants.student_id == current_student.id).first()
        if current_student == None:
            return "404 - Not Found"
        elif current_exam_results != None:
            return f"400 - bad request ( table exam_results)"
        elif current_registration != None:
            return "400 - bad request ( table registrations) "
        else:
            delete_data(current_student)
            session.commit()
            return "success"
    except Exception:
        session.rollback()
        if current_student == None:
            return errors["404"][0],errors["404"][1]
        return errors["405"][0],errors["405"][1]
    finally:
        session.close()

@token_required
def get_all_students(f,key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """show all students

    method to get data student # noqa: E501


    :rtype: List[Students]
    """
    if check_authorization(f,"can_view_all_students") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    rows,number_of_records = get_all_data(Students_instants)
    if rows == None:
        return errors["400"][0],errors["400"][1]
    if key_word:
        rows= rows.filter(or_(Students_instants.address.like(f'%{key_word}%'),Students_instants.email.like(f'%{key_word}%'),Students_instants.full_name.like(f'%{key_word}%'),Students_instants.facebook.like(f'%{key_word}%'),Students_instants.phone.like(f'%{key_word}%'),Students_instants.note.like(f'%{key_word}%')))
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
        data.append({
            "address": item.address,
            "birthday": item.birthday,
            "create_date": item.create_date,
            "email": item.email,
            "facebook": item.facebook,
            "full_name": item.full_name,
            "note": item.note,
            "phone": item.phone,
            "id": item.id
        })
    return 'data'

@token_required
def get_student_by_id(f,student_id):  # noqa: E501
    """Show detail a student by id

    method to show info a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: Students
    """
    if check_authorization(f,"can_view_student_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    item= session.query(Students_instants).filter(Students_instants.id == student_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    data= {
            "address": item.address,
            "birthday": item.birthday,
            "create_date": item.create_date,
            "email": item.email,
            "facebook": item.facebook,
            "full_name": item.full_name,
            "note": item.note,
            "phone": item.phone,
            "id": item.id
        }
    return data

@token_required
def update_student(f,body):  # noqa: E501
   
    """method to update

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if check_authorization(f,"can_update_student") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = [Students.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_student= session.query(Students_instants).filter(Students_instants.id == body.id).first()
        current_student.address= body.address,
        current_student.birthday= body.birthday,
        current_student.create_date= body.create_date,
        current_student.email=body.email,
        current_student.facebook= body.facebook,
        current_student.full_name= body.full_name,
        current_student.note= body.note,
        current_student.phone= body.phone
        session.commit()
        return body
    except Exception:
        session.rollback()  
        return errors["404"][0],errors["404"][1]
    finally:
        session.close()
