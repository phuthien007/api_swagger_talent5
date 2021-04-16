import connexion
import six

from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server import util


def add_class(body):  # noqa: E501
    """add a class

    method to add a class # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: Classes
    """
    if connexion.request.is_json:
        body = [Classes.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def del_class_by_id(class_id):  # noqa: E501
    """delete a class by id

    method to delete a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_classes(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all classes

    method to get data course # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Classes]
    """
    return 'do some magic!'


def get_classes_by_id(class_id):  # noqa: E501
    """Show detail a class by id

    method to show info a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: Classes
    """
    return 'do some magic!'


def update_class(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Classes.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
