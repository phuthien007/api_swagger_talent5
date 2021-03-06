# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, password: str=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param username: The username of this Body.  # noqa: E501
        :type username: str
        :param password: The password of this Body.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'username': str,
            'password': str
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password'
        }
        self._username = username
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this Body.

        fill username  # noqa: E501

        :return: The username of this Body.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Body.

        fill username  # noqa: E501

        :param username: The username of this Body.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this Body.

        fill password  # noqa: E501

        :return: The password of this Body.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Body.

        fill password  # noqa: E501

        :param password: The password of this Body.
        :type password: str
        """

        self._password = password
