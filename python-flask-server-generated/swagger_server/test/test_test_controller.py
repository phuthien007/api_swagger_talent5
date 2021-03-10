# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server.models.teachers import Teachers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTestController(BaseTestCase):
    """TestController integration test stubs"""

    def test_api_classes_get(self):
        """Test case for api_classes_get

        show all classes
        """
        response = self.client.open(
            '/api/classes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_courses_get(self):
        """Test case for api_courses_get

        show all courses
        """
        response = self.client.open(
            '/api/courses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_teachers_get(self):
        """Test case for api_teachers_get

        show all teachers
        """
        response = self.client.open(
            '/api/teachers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
