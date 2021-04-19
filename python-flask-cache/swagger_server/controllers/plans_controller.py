import connexion
import six

from swagger_server.controllers import courses_controller
from swagger_server.models.plans import Plans  # noqa: E501
from swagger_server import util
from swagger_server.controllers.users_controller import *
from swagger_server.controllers.utils import *
from sqlalchemy import or_, and_
from swagger_server.controllers import *


@token_required
@lru_cache(maxsize=None)
def add_plan(f, body):  # noqa: E501

    """add a plan

    method to add a plan # noqa: E501

    :param body: create plan object
    :type body: dict | bytes

    :rtype: Plans
    """
    if check_authorization(f, "can_add_plan") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    if connexion.request.is_json:
        body = Plans.from_dict(connexion.request.get_json())  # noqa: E501
    if not body:
        return jsonify({"message": "data not exist"}), 404
    item = session.query(Plans_instants).filter(Plans_instants.course_id == body.course.id,
                                                Plans_instants.name == body.name).first()
    if item:
        return jsonify({"message": "the plan is exist"}), 400

    try:
        data_course = courses_controller.get_course_by_id(body.course.id)
        new_plan = Plans_instants(course_id=body.course.id, name=body.name)
        add_data(new_plan)
        item = session.query(Plans_instants).filter(Plans_instants.course_id == body.course.id,
                                                    Plans_instants.name == body.name).first()
        if not item:
            return errors["400"][0], errors["400"][1]
        return jsonify({
            "course": data_course,
            "name": item.name,
            "id": item.id
        })
    except Exception as e:

        return jsonify({"message": f"{e}"}), 400


@token_required
@lru_cache(maxsize=None)
def del_plan_by_id(f, plan_id):  # noqa: E501

    """delete a plan by id

    method to delete a plan by plan_id # noqa: E501

    :param plan_id: fill in id a plan_id
    :type plan_id: int

    :rtype: None
    """
    if check_authorization(f, "can_delete_plan_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    item = session.query(Plans_instants).filter(Plans_instants.id == plan_id).first()
    if item == None:
        return errors["404"][0], errors["404"][1]
    delete_data(item)
    return 'success'


@token_required
@lru_cache(maxsize=None)
def get_all_plans(f, key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """show all plans

    method to get data plans # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Plans]
    
    """
    if check_authorization(f, "can_view_all_plans") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    rows, number_of_records = get_all_data(Plans_instants)
    if not rows:
        return jsonify({"message": "not data"}), 400
    if key_word:
        try:
            key_word = int(key_word)
            rows = rows.filter(Plans_instants.course_id == key_word)
        except:
            rows = rows.filter((Plans_instants.name.like(f"%{key_word}%")))
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
        data_course = courses_controller.get_course_by_id(item.course_id)
        data.append({
            "course": data_course,
            "name": item.name,
            "id": item.id
        })
    return data, 200, {"total_of_records": number_of_records, "total_of_pages": total_pages}


@token_required
@lru_cache(maxsize=None)
def get_plan_by_id(f, plan_id):  # noqa: E501

    """Show detail a plan by id

    method to show info a plan by plan_id # noqa: E501

    :param plan_id: fill in id a plan
    :type plan_id: int

    :rtype: Plans
    """
    if check_authorization(f, "can_view_plan_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    item = session.query(Plans_instants).filter(Plans_instants.id == plan_id).first()
    if item == None:
        return errors["404"][0], errors["404"][1]
    data_course = courses_controller.get_course_by_id(item.course_id)
    data = {
        "course": data_course,
        "name": item.name,
        "id": item.id
    }
    return data


@token_required
@lru_cache(maxsize=None)
def update_plan(f, body):  # noqa: E501

    """method to update

     # noqa: E501

    :param body: update plan object
    :type body: dict | bytes

    :rtype: None
    """
    if check_authorization(f, "can_update_plan") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = Plans.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body.id:
        return jsonify({"message": "missing data"}), 400
    try:
        data_course = courses_controller.get_course_by_id(body.course.id)
        item = session.query(Plans_instants).filter(Plans_instants.id == body.id).first()
        item.course_id = data_course['id']
        item.name = body.name
        session.commit()
        return body
    except Exception as e:
        return jsonify({"message": f"{e}"}), 400
