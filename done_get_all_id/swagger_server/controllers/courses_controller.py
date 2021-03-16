import connexion
import six

from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

courses= "courses"
def add_course(body):  # noqa: E501
    """add a course

    method to add a course # noqa: E501

    :param body: create course object
    :type body: dict | bytes

    :rtype: Courses
    """
    if connexion.request.is_json:
        body = [Courses.from_dict(connexion.request.get_json())][0]  # noqa: E501
    new_course= Courses_instants(name=body.name, type= body.type,create_date= body.create_date)
    add_data(new_course)
    return body


def del_course_by_id(course_id):  # noqa: E501
    """delete a course by id

    method to delete a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: None
    """
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
        return "404 not found"
    finally:
        session.close()


def get_all_courses():  # noqa: E501
    """show all courses

    method to get data course # noqa: E501


    :rtype: List[Courses]
    """
    rows = get_all_data(Courses_instants)
    if rows == None:
        return "Not data"
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
    item= session.query(Courses_instants).filter(Courses_instants.course_id == course_id).first()
    if item == None:
        return "Not data"
    data= {
        "course_id": item.course_id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
        }
    return data

def update_course(body):  # noqa: E501
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
        return "fail"
        session.rollback()  
    finally:
        session.close()
