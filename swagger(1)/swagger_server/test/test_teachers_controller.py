# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTeachersController(BaseTestCase):
    """TeachersController integration test stubs"""

    def test_add_teacher(self):
        """Test case for add_teacher

        add a teacher
        """
        body = Teachers()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_teacher_by_id(self):
        """Test case for del_teacher_by_id

        delete a teacher by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers/{teacher_id}'.format(teacher_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_teachers(self):
        """Test case for get_all_teachers

        show all teachers
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_teacher_by_id(self):
        """Test case for get_teacher_by_id

        Show detail a teacher by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers/{teacher_id}'.format(teacher_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_teacher(self):
        """Test case for update_teacher

        method to update
        """
        body = Teachers()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
