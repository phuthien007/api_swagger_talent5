import connexion
import six
from swagger_server.controllers.users_controller import *
from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import *
from sqlalchemy import or_, and_
import time
from datetime import datetime
from swagger_server.controllers import *


@token_required
@lru_cache(maxsize=None)
def add_course(f, body):  # noqa: E501
    if check_authorization(f, "can_add_course") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    """add a course

    method to add a course # noqa: E501

    :param body: create course object
    :type body: dict | bytes

    :rtype: Courses
    """
    if connexion.request.is_json:
        body = Courses.from_dict(connexion.request.get_json())  # noqa: E501
    # try:
    item = session.query(Courses_instants).filter(
        and_(Courses_instants.name == body.name, Courses_instants.type == body.type,
             Courses_instants.create_date == body.create_date)).first()
    if item:
        return jsonify({"message": "The course is exist"}), 400
    new_course = Courses_instants(name=body.name, type=body.type, create_date=body.create_date)
    add_data(new_course)
    # return body
    item = session.query(Courses_instants).filter(
        and_(Courses_instants.name == body.name, Courses_instants.type == body.type,
             Courses_instants.create_date == body.create_date)).first()
    if item == None:
        return errors["404"][0], errors["404"][1]
    data = {
        "id": item.id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
    }
    return data
    # except Exception:
    #     return errors["400"][0],errors["400"][1]


@token_required
@lru_cache(maxsize=None)
def del_course_by_id(f, course_id):  # noqa: E501
    """delete a course by id

    method to delete a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: None
    """
    if check_authorization(f, "can_delete_course_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    try:
        current_course = session.query(Courses_instants).filter(Courses_instants.id == course_id).first()
        current_class = session.query(Classes_instants).filter(Classes_instants.course_id == current_course.id).first()
        current_exam = session.query(Exams_instants).filter(Exams_instants.course_id == course_id).first()
        current_plan = session.query(Plans_instants.course_id == course_id).first()
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
            return errors["404"][0], errors["404"][1]
        return errors["405"][0], errors["405"][1]
    finally:
        session.close()


@token_required
@lru_cache(maxsize=None)
def get_all_courses(f, type_name=None, key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """show all courses

    method to get data course # noqa: E501


    :rtype: List[Courses]
    """
    start_time = datetime.utcnow()
    if check_authorization(f, "can_view_all_courses") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    rows, number_of_records = get_all_data(Courses_instants)
    if rows == None:
        return errors["400"][0], errors["400"][1]
    if key_word:
        rows = rows.filter(
            or_(Courses_instants.name.like(f'%{key_word}%'), Courses_instants.type.like(f'%{key_word}%')))
    total_pages = number_of_records // 20 + 1
    records_per_page = 0 if records_per_page < 0 else records_per_page
    if records_per_page >= 0:
        if page_num >= 0:
            rows = rows.offset(records_per_page * page_num)
            if number_of_records > records_per_page and int(records_per_page) != 20:
                number_of_records = int(records_per_page)
            total_pages = number_of_records // 20 + 1
            if records_per_page > 20:
                records_per_page = 20
            rows = rows.limit(records_per_page)
    data = []
    for item in rows:
        data.append({
            "id": item.id,
            "create_date": item.create_date,
            "name": item.name,
            "type": item.type
        })
    end_time = datetime.utcnow()
    print("time: " + str(end_time - start_time))
    return data, 200, {"total_of_records": number_of_records, "total_of_pages": total_pages}


@token_required
@lru_cache(maxsize=None)
def get_course_by_id(f, course_id):  # noqa: E501
    """Show detail a course by id

    method to show info a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: Courses
    """
    if check_authorization(f, "can_view_course_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    item = session.query(Courses_instants).filter(Courses_instants.id == course_id).first()
    if item == None:
        return errors["404"][0], errors["404"][1]
    data = {
        "id": item.id,
        "create_date": item.create_date,
        "name": item.name,
        "type": item.type
    }
    return data


@token_required
@lru_cache(maxsize=None)
def update_course(f, body):  # noqa: E501
    if check_authorization(f, "can_update_course") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    """method to update

     # noqa: E501

    :param body: update course object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Courses.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_course = session.query(Courses_instants).filter(Courses_instants.id == body.id).first()
        current_course.name = body.name,
        current_course.type = body.type,
        current_course.create_date = body.create_date,
        session.commit()
        return body
    except Exception:
        session.rollback()
        return errors["404"][0], errors["404"][1]
    finally:
        session.close()
