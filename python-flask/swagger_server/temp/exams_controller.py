import connexion
import six

from swagger_server.models.exams import Exams  # noqa: E501
from swagger_server import util


def add_exam(body):  # noqa: E501
    """add a exam

    method to add a exam # noqa: E501

    :param body: create exam object
    :type body: dict | bytes

    :rtype: Exams
    """
    if connexion.request.is_json:
        body = Exams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_exam_by_id(exam_id):  # noqa: E501
    """delete a exam by id

    method to delete a exam by exam_id # noqa: E501

    :param exam_id: fill in id a exam
    :type exam_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_exams(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all exams

    method to get data exam # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Exams]
    """
    return 'do some magic!'


def get_exam_by_id(exam_id):  # noqa: E501
    """Show detail a exam by id

    method to show info a exam by exam_id # noqa: E501

    :param exam_id: fill in id a event
    :type exam_id: int

    :rtype: Exams
    """
    return 'do some magic!'


def update_exam(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update exam object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Exams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
