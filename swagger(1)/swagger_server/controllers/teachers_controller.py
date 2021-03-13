import connexion
import six

from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

teachers = "teachers"

def add_teacher(body):  # noqa: E501
    """add a teacher

    method to add a teacher # noqa: E501

    :param body: create teacher object
    :type body: dict | bytes

    :rtype: Teachers
    """
    if connexion.request.is_json:
        body = Teachers.from_dict(connexion.request.get_json())  # noqa: E501
   # full_name= body["full_name"]
    full_name = body.full_name
    email =body.email
    phone =body.phone
    address =body.address
    grade =body.grade
    sql = f'''
    INSERT INTO {teachers}(full_name, email, phone, address,grade)
    VALUES ('{full_name}','{email}','{phone}','{address}','{grade}')
    '''
    flag= add_data(sql)
    '''if flag == True:
        return body
    else:
        return "add failed"'''
    return flag


def del_teacher_by_id(teacher_id):  # noqa: E501
    """delete a teacher by id

    method to delete a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: None
    """

    return 'do some magic!'


def get_all_teachers():  # noqa: E501
    """show all teachers

    method to get data teacher # noqa: E501


    :rtype: List[Teachers]
    """
    
    rows = get_all_data(teachers)
    if rows == None:
        return "Not data"
    data=[]
    for item in rows.fetchall():
        data.append({
            "address": item[4],
            "email": item[2],
            "full_name": item[1],
            "grade": item[5],
            "phone": item[3],
            "teacher_id": item[0]
        })
    return data


def get_teacher_by_id(teacher_id):  # noqa: E501
    """Show detail a teacher by id

    method to show info a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: Teachers
    """
    item= get_data_by_id("teacher", teacher_id)
    if item == None:
        return "Not data"
    data= {
        "address": item[4],
        "email": item[2],
        "full_name": item[1],
        "grade": item[5],
        "phone": item[3],
        "teacher_id": item[0]
    }
    return data


def update_teacher(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update teacher object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Teachers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
