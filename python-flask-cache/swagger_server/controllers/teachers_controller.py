import connexion
import six
import http.server
from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import *
from swagger_server.controllers.users_controller import *
from sqlalchemy import or_, and_


@token_required
@lru_cache(maxsize=None)
def add_teacher(f, body):  # noqa: E501

    """add a teacher

    method to add a teacher # noqa: E501

    :param body: create teacher object
    :type body: dict | bytes

    :rtype: Teachers
    """

    if check_authorization(f, "can_add_teacher") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    try:
        if connexion.request.is_json:
            body = [Teachers.from_dict(connexion.request.get_json())][0]  # get only teacher into body
        # full_name= body["full_name"]
        item = session.query(Teachers_instants).filter(
            and_(Teachers_instants.full_name == body.full_name, Teachers_instants.address == body.address,
                 Teachers_instants.email == body.email, Teachers_instants.grade == body.grade,
                 Teachers_instants.phone == body.phone)).first()
        if item:
            return jsonify({"message": "the teacher is exist"}), 400
        new_teacher = Teachers_instants(full_name=body.full_name, address=body.address, email=body.email,
                                        grade=body.grade, phone=body.phone)
        add_data(new_teacher)
        item = session.query(Teachers_instants).filter(
            and_(Teachers_instants.full_name == body.full_name, Teachers_instants.address == body.address,
                 Teachers_instants.email == body.email, Teachers_instants.grade == body.grade,
                 Teachers_instants.phone == body.phone)).first()
        data = {
            "address": item.address,
            "email": item.email,
            "full_name": item.full_name,
            "grade": item.grade,
            "phone": item.phone,
            "id": item.id
        }
        return data
    except Exception:
        return errors["400"][0], errors["400"][1]


@token_required
@lru_cache(maxsize=None)
def del_teacher_by_id(f, teacher_id):  # noqa: E501
    """delete a teacher by id

    method to delete a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: None
    """
    if check_authorization(f, "can_delete_teacher_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    current_teacher = session.query(Teachers_instants).filter(Teachers_instants.id == teacher_id).first()
    if not current_teacher:
        return jsonify({'message': 'teacher does not exist'}), 401
    current_class = session.query(Classes_instants).filter(Classes_instants.teacher_id == current_teacher.id).first()

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
            return errors["404"][0], errors["404"][1]
        return errors["405"][0], errors["405"][1]

    finally:
        session.close()


# get all data from table teacher
@token_required
@lru_cache(maxsize=None)
def get_all_teachers(f, type_name=None, key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """show all teachers

    method to get data teacher # noqa: E501


    :rtype: List[Teachers]
    """
    if check_authorization(f, "can_view_all_teachers") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    rows, number_of_records = get_all_data(Teachers_instants)
    if rows == None:
        # when execute fail
        return errors["400"][0], errors["400"][1]
    if key_word and type_name:
        if type_name == 'full_name':
            rows = rows.filter(Teachers_instants.full_name.like(f'%{key_word}%'))
        if type_name == 'email':
            rows = rows.filter(Teachers_instants.email.like(f'%{key_word}%'))
        if type_name == 'phone':
            rows = rows.filter(Teachers_instants.phone.like(f'%{key_word}%'))
        if type_name == 'grade':
            rows = rows.filter(Teachers_instants.grade.like(f'%{key_word}%'))
        if type_name == 'address':
            rows = rows.filter(Teachers_instants.address.like(f'%{key_word}%'))
    elif key_word:
        rows = rows.filter(
            or_(Teachers_instants.address.like(f'%{key_word}%'), Teachers_instants.email.like(f'%{key_word}%'),
                Teachers_instants.full_name.like(f'%{key_word}%'), Teachers_instants.grade.like(f'%{key_word}%'),
                Teachers_instants.phone.like(f'%{key_word}%')))

    total_pages = number_of_records // 20 + 1
    print(number_of_records)
    records_per_page = 0 if records_per_page < 0 else records_per_page
    print(number_of_records)

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
            "address": item.address,
            "email": item.email,
            "full_name": item.full_name,
            "grade": item.grade,
            "phone": item.phone,
            "id": item.id
        })
    return data, 200, {"total_of_records": number_of_records, "total_of_pages": total_pages}


@token_required
@lru_cache(maxsize=None)
def get_teacher_by_id(f, teacher_id):  # noqa: E501
    """Show detail a teacher by id

    method to show info a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: Teachers
    """
    # query data from database through orm api session
    if check_authorization(f, "can_view_teacher_by_id") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400
    try:
        item = session.query(Teachers_instants).filter(Teachers_instants.id == teacher_id).first()
        data = {
            "address": item.address,
            "email": item.email,
            "full_name": item.full_name,
            "grade": item.grade,
            "phone": item.phone,
            "id": item.id
        }
        return data
    except Exception as e:
        print(e)
        session.rollback()
        return errors["404"][0], errors["404"][1]
    finally:
        session.close()


@token_required
@lru_cache(maxsize=None)
def update_teacher(f, body):  # noqa: E501

    """method to update

     # noqa: E501

    :param body: update teacher object
    :type body: dict | bytes

    :rtype: None
    """
    if check_authorization(f, "can_update_teacher") == False:
        return jsonify({"message": "the user dont has permision to request"}), 400

    if connexion.request.is_json:
        body = [Teachers.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_teacher = session.query(Teachers_instants).filter(Teachers_instants.id == body.id).first()
        current_teacher.address = body.address,
        current_teacher.email = body.email,
        current_teacher.full_name = body.full_name,
        current_teacher.grade = body.grade,
        current_teacher.phone = body.phone
        session.commit()
        return body
    except Exception:
        session.rollback()
        return errors["404"][0], errors["404"][1]
    finally:
        session.close()
