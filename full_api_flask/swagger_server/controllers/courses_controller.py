import connexion
import six
from swagger_server.controllers.users_controller import*
from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*
from sqlalchemy import or_,and_

from swagger_server.controllers import *

def add_course(body):  # noqa: E501
    f= ""
    token_required(f)
    """add a course

    method to add a course # noqa: E501

    :param body: create course object
    :type body: dict | bytes

    :rtype: Courses
    """
    if connexion.request.is_json:
        body = Courses.from_dict(connexion.request.get_json())  # noqa: E501
    # try:
    item= session.query(Courses_instants).filter(and_(Courses_instants.name == body.name, Courses_instants.type == body.type, Courses_instants.create_date == body.create_date)).first()
    if item:
        return jsonify({"message":"The course is exist"}), 400
    new_course= Courses_instants(name=body.name, type= body.type,create_date= body.create_date)
    add_data(new_course)
    # return body
    item= session.query(Courses_instants).filter(and_(Courses_instants.name == body.name, Courses_instants.type == body.type, Courses_instants.create_date == body.create_date)).first()
    print(item)
    if item == None:
        return errors["404"][0],errors["404"][1]
    data= {
        "course_id": item.course_id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
        }
    return data
    # except Exception:
    #     return errors["400"][0],errors["400"][1]


def del_course_by_id(course_id):  # noqa: E501
    """delete a course by id

    method to delete a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: None
    """
    f= ""
    token_required(f)
    try:
        current_course= session.query(Courses_instants).filter(Courses_instants.course_id == course_id).first()
        current_class= session.query(Classes_instants).filter(Classes_instants.course_id == current_course.course_id).first()
        current_exam= session.query(Exams_instants).filter(Exams_instants.course_id == course_id).first()
        current_plan= session.query(Plans_instants.course_id == course_id ).first()
        if current_course == None:
            return "404 - Not Found"
        elif current_class != None:
            return "400 - bad request ( table classes)"
        elif current_exam != None:
            return "400 - bad request ( table exams) "
        elif current_plan != None:
            return "400 - bad request ( table plans)"
        else:
            delete_data(current_course)
            session.commit()
            return "success"
    except Exception:
        session.rollback()
        if current_course == None:
            return errors["404"][0],errors["404"][1]
        return errors["405"][0],errors["405"][1]
    finally:
        session.close()

@token_required
def get_all_courses(f,type_name=None, key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all courses

    method to get data course # noqa: E501


    :rtype: List[Courses]
    """
    rows = get_all_data(Courses_instants)
    if rows == None:
        return errors["400"][0],errors["400"][1]
    if key_word:
        rows= rows.filter(or_(Courses_instants.name.like(f'%{key_word}%'),Courses_instants.type.like(f'%{key_word}%')))
    if records_per_page:
        rows= rows.limit(records_per_page)
        if page_num:
            rows= rows.offset(records_per_page* page_num)
    data=[]
    for item in rows:
        data.append({
        "course_id": item.course_id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
        })
    return data


def get_course_by_id(course_id):  # noqa: E501
    """Show detail a course by id

    method to show info a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: Courses
    """
    f= ""
    token_required(f)
    item= session.query(Courses_instants).filter(Courses_instants.course_id == course_id).first()
    if item == None:
        return errors["404"][0],errors["404"][1]
    data= {
        "course_id": item.course_id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
        }
    return data

def update_course(body):  # noqa: E501
    f= ""
    token_required(f)
    """method to update

     # noqa: E501

    :param body: update course object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Courses.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_course= session.query(Courses_instants).filter(Courses_instants.course_id == body.course_id).first()
        current_course.name= body.name,
        current_course.type= body.type,
        current_course.create_date= body.create_date,
        session.commit()
        return body
    except Exception:
        session.rollback()  
        return errors["404"][0],errors["404"][1]
    finally:
        session.close()
