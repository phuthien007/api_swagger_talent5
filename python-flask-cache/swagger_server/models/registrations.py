# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.classes import Classes  # noqa: F401,E501
from swagger_server.models.students import Students  # noqa: F401,E501
from swagger_server import util


class Registrations(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, student: Students=None, _class: Classes=None, register_day: datetime=None, status: str=None, create_date: datetime=None):  # noqa: E501
        """Registrations - a model defined in Swagger

        :param student: The student of this Registrations.  # noqa: E501
        :type student: Students
        :param _class: The _class of this Registrations.  # noqa: E501
        :type _class: Classes
        :param register_day: The register_day of this Registrations.  # noqa: E501
        :type register_day: datetime
        :param status: The status of this Registrations.  # noqa: E501
        :type status: str
        :param create_date: The create_date of this Registrations.  # noqa: E501
        :type create_date: datetime
        """
        self.swagger_types = {
            'student': Students,
            '_class': Classes,
            'register_day': datetime,
            'status': str,
            'create_date': datetime
        }

        self.attribute_map = {
            'student': 'student',
            '_class': 'class',
            'register_day': 'register_day',
            'status': 'status',
            'create_date': 'create_date'
        }
        self._student = student
        self.__class = _class
        self._register_day = register_day
        self._status = status
        self._create_date = create_date

    @classmethod
    def from_dict(cls, dikt) -> 'Registrations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The registrations of this Registrations.  # noqa: E501
        :rtype: Registrations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def student(self) -> Students:
        """Gets the student of this Registrations.


        :return: The student of this Registrations.
        :rtype: Students
        """
        return self._student

    @student.setter
    def student(self, student: Students):
        """Sets the student of this Registrations.


        :param student: The student of this Registrations.
        :type student: Students
        """
        if student is None:
            raise ValueError("Invalid value for `student`, must not be `None`")  # noqa: E501

        self._student = student

    @property
    def _class(self) -> Classes:
        """Gets the _class of this Registrations.


        :return: The _class of this Registrations.
        :rtype: Classes
        """
        return self.__class

    @_class.setter
    def _class(self, _class: Classes):
        """Sets the _class of this Registrations.


        :param _class: The _class of this Registrations.
        :type _class: Classes
        """
        if _class is None:
            raise ValueError("Invalid value for `_class`, must not be `None`")  # noqa: E501

        self.__class = _class

    @property
    def register_day(self) -> datetime:
        """Gets the register_day of this Registrations.


        :return: The register_day of this Registrations.
        :rtype: datetime
        """
        return self._register_day

    @register_day.setter
    def register_day(self, register_day: datetime):
        """Sets the register_day of this Registrations.


        :param register_day: The register_day of this Registrations.
        :type register_day: datetime
        """

        self._register_day = register_day

    @property
    def status(self) -> str:
        """Gets the status of this Registrations.


        :return: The status of this Registrations.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Registrations.


        :param status: The status of this Registrations.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def create_date(self) -> datetime:
        """Gets the create_date of this Registrations.


        :return: The create_date of this Registrations.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime):
        """Sets the create_date of this Registrations.


        :param create_date: The create_date of this Registrations.
        :type create_date: datetime
        """

        self._create_date = create_date
