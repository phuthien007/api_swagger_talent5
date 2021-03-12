# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.students import Students  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentsController(BaseTestCase):
    """StudentsController integration test stubs"""

    def test_add_student(self):
        """Test case for add_student

        add a student
        """
        body = Students()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/students',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_student_by_id(self):
        """Test case for del_student_by_id

        delete a student by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/students/{student_id}'.format(student_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_students(self):
        """Test case for get_all_students

        show all students
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/students',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student_by_id(self):
        """Test case for get_student_by_id

        Show detail a student by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/students/{student_id}'.format(student_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student(self):
        """Test case for update_student

        method to update
        """
        body = Students()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/students',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
