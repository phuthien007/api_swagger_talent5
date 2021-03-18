import connexion
import six
import http.server
from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

from sqlalchemy import or_,and_
def add_teacher(body):  # noqa: E501
    """add a teacher

    method to add a teacher # noqa: E501

    :param body: create teacher object
    :type body: dict | bytes

    :rtype: Teachers
    """
    try:
        if connexion.request.is_json:
            body = [Teachers.from_dict(connexion.request.get_json())][0]  # get only teacher into body
    # full_name= body["full_name"]
        new_teacher= Teachers_instants(full_name=body.full_name, address= body.address,email= body.email,grade= body.grade,phone=body.phone)
        add_data(new_teacher)
        item= session.query(Teachers_instants).filter(and_(Teachers_instants.full_name == body.full_name, Teachers_instants.address == body.address,Teachers_instants.email == body.email,Teachers_instants.grade == body.grade,Teachers_instants.phone == body.phone)).first()
        data= {
                "address": item.address,
                "email": item.email,
                "full_name": item.full_name,
                "grade": item.grade,
                "phone": item.phone,
                "teacher_id": item.teacher_id
            }
        return data
    except Exception :
        return errors["400"][0],errors["400"][1]

def del_teacher_by_id(teacher_id):  # noqa: E501
    """delete a teacher by id

    method to delete a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: None
    """
    current_teacher= session.query(Teachers_instants).filter(Teachers_instants.teacher_id == teacher_id).first()
    current_class= session.query(Classes_instants).filter(Classes_instants.teacher_id == current_teacher.teacher_id).first()
        
    try:
        if current_teacher == None:
            return "404 - Not Found"
        elif current_class != None:
            return "400 - bad request (table classes)"
        else:
            delete_data(current_teacher)
            session.commit()
            return "success"
    except Exception:
        session.rollback()
        if current_teacher == None:
            return errors["404"][0],errors["404"][1]
        return errors["405"][0],errors["405"][1]

    finally:
        session.close()
# get all data from table teacher
def get_all_teachers(type_name=None, key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all teachers

    method to get data teacher # noqa: E501


    :rtype: List[Teachers]
    """
    rows = get_all_data(Teachers_instants)
    if rows == None:
        # when execute fail
        return errors["400"][0],errors["400"][1]
    if key_word and type_name:
        if type_name == 'full_name':
            rows= rows.filter(Teachers_instants.full_name.like(f'%{key_word}%'))
        if type_name == 'email':
            rows= rows.filter(Teachers_instants.email.like(f'%{key_word}%'))
        if type_name == 'phone':
            rows= rows.filter(Teachers_instants.phone.like(f'%{key_word}%'))
        if type_name == 'grade':
            rows= rows.filter(Teachers_instants.grade.like(f'%{key_word}%'))
        if type_name == 'address':
            rows= rows.filter(Teachers_instants.address.like(f'%{key_word}%'))
    elif key_word:
        rows= rows.filter(or_(Teachers_instants.address.like(f'%{key_word}%'),Teachers_instants.email.like(f'%{key_word}%'),Teachers_instants.full_name.like(f'%{key_word}%'),Teachers_instants.grade.like(f'%{key_word}%'),Teachers_instants.phone.like(f'%{key_word}%')))
    if records_per_page:
        rows= rows.limit(records_per_page)
        if page_num:
            rows= rows.offset(records_per_page* page_num)
    data=[] 
    for item in rows:
        data.append({
            "address": item.address,
            "email": item.email,
            "full_name": item.full_name,
            "grade": item.grade,
            "phone": item.phone,
            "teacher_id": item.teacher_id
        })
    return data


def get_teacher_by_id(teacher_id):  # noqa: E501
    """Show detail a teacher by id

    method to show info a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: Teachers
    """
    # query data from database through orm api session
    try:
        item= session.query(Teachers_instants).filter(Teachers_instants.teacher_id == teacher_id).first()
        data= {
                "address": item.address,
                "email": item.email,
                "full_name": item.full_name,
                "grade": item.grade,
                "phone": item.phone,
                "teacher_id": item.teacher_id
            }
        return data
    except Exception as e:
        session.rollback()
        return  errors["404"][0],errors["404"][1]
    finally:
        session.close()

def update_teacher(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update teacher object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Teachers.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_teacher= session.query(Teachers_instants).filter(Teachers_instants.teacher_id == body.teacher_id).first()
        current_teacher.address= body.address,
        current_teacher.email= body.email,
        current_teacher.full_name= body.full_name,
        current_teacher.grade=body.grade,
        current_teacher.phone=body.phone
        session.commit()
        return body
    except Exception:
        session.rollback()
        return errors["404"][0],errors["404"][1]
    finally:
        session.close()
