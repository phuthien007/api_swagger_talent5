# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Users(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_id: int=None, username: str=None, email: str=None, password: str=None, fullname: str=None, birthday: date=None, last_login_date: datetime=None, lockout_date: datetime=None, login_failed_count: float=None, register_date: datetime=None, forgot_password_token: str=None):  # noqa: E501
        """Users - a model defined in Swagger

        :param user_id: The user_id of this Users.  # noqa: E501
        :type user_id: int
        :param username: The username of this Users.  # noqa: E501
        :type username: str
        :param email: The email of this Users.  # noqa: E501
        :type email: str
        :param password: The password of this Users.  # noqa: E501
        :type password: str
        :param fullname: The fullname of this Users.  # noqa: E501
        :type fullname: str
        :param birthday: The birthday of this Users.  # noqa: E501
        :type birthday: date
        :param last_login_date: The last_login_date of this Users.  # noqa: E501
        :type last_login_date: datetime
        :param lockout_date: The lockout_date of this Users.  # noqa: E501
        :type lockout_date: datetime
        :param login_failed_count: The login_failed_count of this Users.  # noqa: E501
        :type login_failed_count: float
        :param register_date: The register_date of this Users.  # noqa: E501
        :type register_date: datetime
        :param forgot_password_token: The forgot_password_token of this Users.  # noqa: E501
        :type forgot_password_token: str
        """
        self.swagger_types = {
            'user_id': int,
            'username': str,
            'email': str,
            'password': str,
            'fullname': str,
            'birthday': date,
            'last_login_date': datetime,
            'lockout_date': datetime,
            'login_failed_count': float,
            'register_date': datetime,
            'forgot_password_token': str
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'fullname': 'fullname',
            'birthday': 'birthday',
            'last_login_date': 'last_login_date',
            'lockout_date': 'lockout_date',
            'login_failed_count': 'login_failed_count',
            'register_date': 'register_date',
            'forgot_password_token': 'forgot_password_token'
        }
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password
        self._fullname = fullname
        self._birthday = birthday
        self._last_login_date = last_login_date
        self._lockout_date = lockout_date
        self._login_failed_count = login_failed_count
        self._register_date = register_date
        self._forgot_password_token = forgot_password_token

    @classmethod
    def from_dict(cls, dikt) -> 'Users':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The users of this Users.  # noqa: E501
        :rtype: Users
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Users.


        :return: The user_id of this Users.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Users.


        :param user_id: The user_id of this Users.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def username(self) -> str:
        """Gets the username of this Users.


        :return: The username of this Users.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Users.


        :param username: The username of this Users.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this Users.


        :return: The email of this Users.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Users.


        :param email: The email of this Users.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this Users.


        :return: The password of this Users.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Users.


        :param password: The password of this Users.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def fullname(self) -> str:
        """Gets the fullname of this Users.


        :return: The fullname of this Users.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname: str):
        """Sets the fullname of this Users.


        :param fullname: The fullname of this Users.
        :type fullname: str
        """
        if fullname is None:
            raise ValueError("Invalid value for `fullname`, must not be `None`")  # noqa: E501

        self._fullname = fullname

    @property
    def birthday(self) -> date:
        """Gets the birthday of this Users.


        :return: The birthday of this Users.
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: date):
        """Sets the birthday of this Users.


        :param birthday: The birthday of this Users.
        :type birthday: date
        """

        self._birthday = birthday

    @property
    def last_login_date(self) -> datetime:
        """Gets the last_login_date of this Users.


        :return: The last_login_date of this Users.
        :rtype: datetime
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date: datetime):
        """Sets the last_login_date of this Users.


        :param last_login_date: The last_login_date of this Users.
        :type last_login_date: datetime
        """

        self._last_login_date = last_login_date

    @property
    def lockout_date(self) -> datetime:
        """Gets the lockout_date of this Users.


        :return: The lockout_date of this Users.
        :rtype: datetime
        """
        return self._lockout_date

    @lockout_date.setter
    def lockout_date(self, lockout_date: datetime):
        """Sets the lockout_date of this Users.


        :param lockout_date: The lockout_date of this Users.
        :type lockout_date: datetime
        """

        self._lockout_date = lockout_date

    @property
    def login_failed_count(self) -> float:
        """Gets the login_failed_count of this Users.


        :return: The login_failed_count of this Users.
        :rtype: float
        """
        return self._login_failed_count

    @login_failed_count.setter
    def login_failed_count(self, login_failed_count: float):
        """Sets the login_failed_count of this Users.


        :param login_failed_count: The login_failed_count of this Users.
        :type login_failed_count: float
        """

        self._login_failed_count = login_failed_count

    @property
    def register_date(self) -> datetime:
        """Gets the register_date of this Users.


        :return: The register_date of this Users.
        :rtype: datetime
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date: datetime):
        """Sets the register_date of this Users.


        :param register_date: The register_date of this Users.
        :type register_date: datetime
        """

        self._register_date = register_date

    @property
    def forgot_password_token(self) -> str:
        """Gets the forgot_password_token of this Users.


        :return: The forgot_password_token of this Users.
        :rtype: str
        """
        return self._forgot_password_token

    @forgot_password_token.setter
    def forgot_password_token(self, forgot_password_token: str):
        """Sets the forgot_password_token of this Users.


        :param forgot_password_token: The forgot_password_token of this Users.
        :type forgot_password_token: str
        """

        self._forgot_password_token = forgot_password_token
