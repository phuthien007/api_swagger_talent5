import connexion
import six

from swagger_server.models.students import Students  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*
students="students"

def add_student(body):  # noqa: E501
    """add a student

    method to add a student # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Students
    """
    if connexion.request.is_json:
        body = Students.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_student_by_id(student_id):  # noqa: E501
    """delete a student by id

    method to delete a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_students():  # noqa: E501
    """show all students

    method to get data student # noqa: E501


    :rtype: List[Students]
    """
    rows = get_all_data(students)
    if rows == None:
        return "Not data"
    data=[]
    for item in rows.fetchall():
        data.append({
            "address": item[4],
            "birthday": item[5],
            "create_date": item[8],
            "email": item[2],
            "facebook": item[7],
            "full_name": item[1],
            "note": item[6],
            "phone": item[3],
            "student_id": item[0]
        })
    return data


def get_student_by_id(student_id):  # noqa: E501
    """Show detail a student by id

    method to show info a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: Students
    """
    item = get_data_by_id("student",student_id)
    if item == None:
        return "Not data"
    data={
        "address": item[4],
        "birthday": item[5],
        "create_date": item[8],
        "email": item[2],
        "facebook": item[7],
        "full_name": item[1],
        "note": item[6],
        "phone": item[3],
        "student_id": item[0]
        }
    return data


def update_student(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Students.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
