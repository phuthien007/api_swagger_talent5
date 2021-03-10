import connexion
import six

from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server import util


def api_classes_get():  # noqa: E501
    """show all classes

     # noqa: E501


    :rtype: Classes
    """
    return 'do some magic!'


def api_courses_get():  # noqa: E501
    """show all courses

     # noqa: E501


    :rtype: Courses
    """
    return 'do some magic!'


def api_teachers_get():  # noqa: E501
    """show all teachers

    the table teachers # noqa: E501


    :rtype: Teachers
    """
    return 'do some magic!'
