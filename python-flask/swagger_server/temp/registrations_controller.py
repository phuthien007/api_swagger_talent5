import connexion
import six

from swagger_server.models.registrations import Registrations  # noqa: E501
from swagger_server import util


def add_registration(body):  # noqa: E501
    """add a registrations

    method to add a registration # noqa: E501

    :param body: create exam_result object
    :type body: dict | bytes

    :rtype: Registrations
    """
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_registration_by_id(class_id, student_id):  # noqa: E501
    """delete a registration by id

    method to delete a registration by registration_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int
    :param student_id: fill in id a student
    :type student_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_registrations(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all registrations

    method to get data registrations # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Registrations]
    """
    return 'do some magic!'


def get_registration_by_id(class_id, student_id):  # noqa: E501
    """Show detail a registrations by id

    method to show info a registration by registration_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int
    :param student_id: fill in id a student
    :type student_id: int

    :rtype: Registrations
    """
    return 'do some magic!'


def update_registration(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update registration object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Registrations.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
