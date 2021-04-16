import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.users import Users  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_user_by_id(user_id):  # noqa: E501
    """delete a user by id

    method to delete a user by user_id # noqa: E501

    :param user_id: fill in id a user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_users(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """the method to show all users

    you can show all users # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Users]
    """
    return 'do some magic!'


def get_user_by_id(user_id):  # noqa: E501
    """Show detail a user by id

    method to show info a user by student_id # noqa: E501

    :param user_id: fill in id a student
    :type user_id: int

    :rtype: Users
    """
    return 'do some magic!'


def login_user(body=None):  # noqa: E501
    """log user into your system

    method to login user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(body):  # noqa: E501
    """the method to register

    you can register user # noqa: E501

    :param body: body
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Users.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
