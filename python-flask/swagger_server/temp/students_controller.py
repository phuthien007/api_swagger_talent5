import connexion
import six

from swagger_server.models.students import Students  # noqa: E501
from swagger_server import util


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


def get_all_students(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all students

    method to get data student # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Students]
    """
    return 'do some magic!'


def get_student_by_id(student_id):  # noqa: E501
    """Show detail a student by id

    method to show info a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: Students
    """
    return 'do some magic!'


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
