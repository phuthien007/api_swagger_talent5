# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Students(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, full_name: str=None, address: str=None, email: str=None, phone: str=None, birthday: date=None, note: str=None, facebook: str=None, create_date: datetime=None):  # noqa: E501
        """Students - a model defined in Swagger

        :param id: The id of this Students.  # noqa: E501
        :type id: int
        :param full_name: The full_name of this Students.  # noqa: E501
        :type full_name: str
        :param address: The address of this Students.  # noqa: E501
        :type address: str
        :param email: The email of this Students.  # noqa: E501
        :type email: str
        :param phone: The phone of this Students.  # noqa: E501
        :type phone: str
        :param birthday: The birthday of this Students.  # noqa: E501
        :type birthday: date
        :param note: The note of this Students.  # noqa: E501
        :type note: str
        :param facebook: The facebook of this Students.  # noqa: E501
        :type facebook: str
        :param create_date: The create_date of this Students.  # noqa: E501
        :type create_date: datetime
        """
        self.swagger_types = {
            'id': int,
            'full_name': str,
            'address': str,
            'email': str,
            'phone': str,
            'birthday': date,
            'note': str,
            'facebook': str,
            'create_date': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'full_name': 'full_name',
            'address': 'address',
            'email': 'email',
            'phone': 'phone',
            'birthday': 'birthday',
            'note': 'note',
            'facebook': 'facebook',
            'create_date': 'create_date'
        }
        self._id = id
        self._full_name = full_name
        self._address = address
        self._email = email
        self._phone = phone
        self._birthday = birthday
        self._note = note
        self._facebook = facebook
        self._create_date = create_date

    @classmethod
    def from_dict(cls, dikt) -> 'Students':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The students of this Students.  # noqa: E501
        :rtype: Students
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Students.


        :return: The id of this Students.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Students.


        :param id: The id of this Students.
        :type id: int
        """

        self._id = id

    @property
    def full_name(self) -> str:
        """Gets the full_name of this Students.


        :return: The full_name of this Students.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        """Sets the full_name of this Students.


        :param full_name: The full_name of this Students.
        :type full_name: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def address(self) -> str:
        """Gets the address of this Students.


        :return: The address of this Students.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Students.


        :param address: The address of this Students.
        :type address: str
        """

        self._address = address

    @property
    def email(self) -> str:
        """Gets the email of this Students.


        :return: The email of this Students.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Students.


        :param email: The email of this Students.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def phone(self) -> str:
        """Gets the phone of this Students.


        :return: The phone of this Students.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this Students.


        :param phone: The phone of this Students.
        :type phone: str
        """

        self._phone = phone

    @property
    def birthday(self) -> date:
        """Gets the birthday of this Students.


        :return: The birthday of this Students.
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: date):
        """Sets the birthday of this Students.


        :param birthday: The birthday of this Students.
        :type birthday: date
        """

        self._birthday = birthday

    @property
    def note(self) -> str:
        """Gets the note of this Students.


        :return: The note of this Students.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str):
        """Sets the note of this Students.


        :param note: The note of this Students.
        :type note: str
        """

        self._note = note

    @property
    def facebook(self) -> str:
        """Gets the facebook of this Students.


        :return: The facebook of this Students.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook: str):
        """Sets the facebook of this Students.


        :param facebook: The facebook of this Students.
        :type facebook: str
        """

        self._facebook = facebook

    @property
    def create_date(self) -> datetime:
        """Gets the create_date of this Students.


        :return: The create_date of this Students.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime):
        """Sets the create_date of this Students.


        :param create_date: The create_date of this Students.
        :type create_date: datetime
        """

        self._create_date = create_date
