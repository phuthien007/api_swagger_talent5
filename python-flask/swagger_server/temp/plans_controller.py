import connexion
import six

from swagger_server.models.plans import Plans  # noqa: E501
from swagger_server import util


def add_plan(body):  # noqa: E501
    """add a plan

    method to add a plan # noqa: E501

    :param body: create plan object
    :type body: dict | bytes

    :rtype: Plans
    """
    if connexion.request.is_json:
        body = Plans.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_plan_by_id(plan_id):  # noqa: E501
    """delete a plan by id

    method to delete a plan by plan_id # noqa: E501

    :param plan_id: fill in id a plan_id
    :type plan_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_plans(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
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
    return 'do some magic!'


def get_plan_by_id(plan_id):  # noqa: E501
    """Show detail a plan by id

    method to show info a plan by plan_id # noqa: E501

    :param plan_id: fill in id a plan
    :type plan_id: int

    :rtype: Plans
    """
    return 'do some magic!'


def update_plan(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update plan object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Plans.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
