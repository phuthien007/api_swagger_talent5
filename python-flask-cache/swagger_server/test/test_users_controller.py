# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.users import Users  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        the method to register
        """
        body = Users()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_user_by_id(self):
        """Test case for del_user_by_id

        delete a user by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/users/{user_id}'.format(user_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_users(self):
        """Test case for get_all_users

        the method to show all users
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Show detail a user by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/users/{user_id}'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        log user into your system
        """
        body = Body()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/user/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        the method to register
        """
        body = Users()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/users',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
