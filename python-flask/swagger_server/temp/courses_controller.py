import connexion
import six

from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server import util


def add_course(body):  # noqa: E501
    """add a course

    method to add a course # noqa: E501

    :param body: create course object
    :type body: dict | bytes

    :rtype: Courses
    """
    if connexion.request.is_json:
        body = Courses.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_course_by_id(course_id):  # noqa: E501
    """delete a course by id

    method to delete a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_courses(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all courses

    method to get data course # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Courses]
    """
    return 'do some magic!'


def get_course_by_id(course_id):  # noqa: E501
    """Show detail a course by id

    method to show info a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: Courses
    """
    return 'do some magic!'


def update_course(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update course object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Courses.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
