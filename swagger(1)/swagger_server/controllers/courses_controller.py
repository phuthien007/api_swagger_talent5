import connexion
import six

from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

courses= "courses"
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


def get_all_courses():  # noqa: E501
    """show all courses

    method to get data course # noqa: E501


    :rtype: List[Courses]
    """
    rows = get_all_data(courses)
    if rows == None:
        return "Not data"
    data=[]
    for item in rows.fetchall():
        data.append({
        "course_id": item[0],
        "create_date": item[3],
        "name": item[1],
        "type": item[2]
        })
    return data


def get_course_by_id(course_id):  # noqa: E501
    """Show detail a course by id

    method to show info a course by course_id # noqa: E501

    :param course_id: fill in id a course
    :type course_id: int

    :rtype: Courses
    """
    data_course= get_data_by_id("course",course_id)
    if data_course == None:
        return "Not data"
    data=  {
        "course_id": data_course[0],
        "create_date": data_course[3],
        "name": data_course[1],
        "type": data_course[2]
        }
    return data


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
