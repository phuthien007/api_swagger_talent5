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

    def test_get_classes(self):
        """Test case for get_classes

        show all classes
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/classes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_course(self):
        """Test case for get_course

        show all courses
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_teacher(self):
        """Test case for get_teacher

        show all teachers
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/teachers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
