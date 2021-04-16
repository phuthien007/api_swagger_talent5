import connexion
import six

from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server import util


def add_teacher(body):  # noqa: E501
    """add a teacher

    method to add a teacher # noqa: E501

    :param body: create teacher object
    :type body: dict | bytes

    :rtype: Teachers
    """
    if connexion.request.is_json:
        body = Teachers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_teacher_by_id(teacher_id):  # noqa: E501
    """delete a teacher by id

    method to delete a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_teachers(type_name=None, key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all teachers

    method to get data teacher # noqa: E501

    :param type_name: you can fill kw you want to search
    :type type_name: str
    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Teachers]
    """
    return 'do some magic!'


def get_teacher_by_id(teacher_id):  # noqa: E501
    """Show detail a teacher by id

    method to show info a teacher by teacher_id # noqa: E501

    :param teacher_id: fill in id a teacher
    :type teacher_id: int

    :rtype: Teachers
    """
    return 'do some magic!'


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
