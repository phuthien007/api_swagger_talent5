# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Teachers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, teacher_id: int=None, full_name: str=None, email: str=None, phone: str=None, address: str=None, grade: str=None):  # noqa: E501
        """Teachers - a model defined in Swagger

        :param teacher_id: The teacher_id of this Teachers.  # noqa: E501
        :type teacher_id: int
        :param full_name: The full_name of this Teachers.  # noqa: E501
        :type full_name: str
        :param email: The email of this Teachers.  # noqa: E501
        :type email: str
        :param phone: The phone of this Teachers.  # noqa: E501
        :type phone: str
        :param address: The address of this Teachers.  # noqa: E501
        :type address: str
        :param grade: The grade of this Teachers.  # noqa: E501
        :type grade: str
        """
        self.swagger_types = {
            'teacher_id': int,
            'full_name': str,
            'email': str,
            'phone': str,
            'address': str,
            'grade': str
        }

        self.attribute_map = {
            'teacher_id': 'teacher_id',
            'full_name': 'full_name',
            'email': 'email',
            'phone': 'phone',
            'address': 'address',
            'grade': 'grade'
        }
        self._teacher_id = teacher_id
        self._full_name = full_name
        self._email = email
        self._phone = phone
        self._address = address
        self._grade = grade

    @classmethod
    def from_dict(cls, dikt) -> 'Teachers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The teachers of this Teachers.  # noqa: E501
        :rtype: Teachers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def teacher_id(self) -> int:
        """Gets the teacher_id of this Teachers.


        :return: The teacher_id of this Teachers.
        :rtype: int
        """
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, teacher_id: int):
        """Sets the teacher_id of this Teachers.


        :param teacher_id: The teacher_id of this Teachers.
        :type teacher_id: int
        """

        self._teacher_id = teacher_id

    @property
    def full_name(self) -> str:
        """Gets the full_name of this Teachers.


        :return: The full_name of this Teachers.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        """Sets the full_name of this Teachers.


        :param full_name: The full_name of this Teachers.
        :type full_name: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def email(self) -> str:
        """Gets the email of this Teachers.
        :return: The email of this Teachers.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Teachers.


        :param email: The email of this Teachers.
        :type email: str
        """

        self._email = email

    @property
    def phone(self) -> str:
        """Gets the phone of this Teachers.


        :return: The phone of this Teachers.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this Teachers.


        :param phone: The phone of this Teachers.
        :type phone: str
        """

        self._phone = phone

    @property
    def address(self) -> str:
        """Gets the address of this Teachers.


        :return: The address of this Teachers.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Teachers.


        :param address: The address of this Teachers.
        :type address: str
        """

        self._address = address

    @property
    def grade(self) -> str:
        """Gets the grade of this Teachers.


        :return: The grade of this Teachers.
        :rtype: str
        """
        return self._grade

    @grade.setter
    def grade(self, grade: str):
        """Sets the grade of this Teachers.


        :param grade: The grade of this Teachers.
        :type grade: str
        """

        self._grade = grade
