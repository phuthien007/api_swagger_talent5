# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.courses import Courses  # noqa: F401,E501
from swagger_server import util


class Plans(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, plan_id: int=None, name: str=None, course_id: Courses=None):  # noqa: E501
        """Plans - a model defined in Swagger

        :param plan_id: The plan_id of this Plans.  # noqa: E501
        :type plan_id: int
        :param name: The name of this Plans.  # noqa: E501
        :type name: str
        :param course_id: The course_id of this Plans.  # noqa: E501
        :type course_id: Courses
        """
        self.swagger_types = {
            'plan_id': int,
            'name': str,
            'course_id': Courses
        }

        self.attribute_map = {
            'plan_id': 'plan_id',
            'name': 'name',
            'course_id': 'course_id'
        }
        self._plan_id = plan_id
        self._name = name
        self._course_id = course_id

    @classmethod
    def from_dict(cls, dikt) -> 'Plans':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The plans of this Plans.  # noqa: E501
        :rtype: Plans
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plan_id(self) -> int:
        """Gets the plan_id of this Plans.


        :return: The plan_id of this Plans.
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id: int):
        """Sets the plan_id of this Plans.


        :param plan_id: The plan_id of this Plans.
        :type plan_id: int
        """

        self._plan_id = plan_id

    @property
    def name(self) -> str:
        """Gets the name of this Plans.


        :return: The name of this Plans.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Plans.


        :param name: The name of this Plans.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def course_id(self) -> Courses:
        """Gets the course_id of this Plans.


        :return: The course_id of this Plans.
        :rtype: Courses
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id: Courses):
        """Sets the course_id of this Plans.


        :param course_id: The course_id of this Plans.
        :type course_id: Courses
        """
        if course_id is None:
            raise ValueError("Invalid value for `course_id`, must not be `None`")  # noqa: E501

        self._course_id = course_id