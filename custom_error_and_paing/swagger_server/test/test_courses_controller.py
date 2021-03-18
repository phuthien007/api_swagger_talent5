# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.courses import Courses  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCoursesController(BaseTestCase):
    """CoursesController integration test stubs"""

    def test_add_course(self):
        """Test case for add_course

        add a course
        """
        body = Courses()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_course_by_id(self):
        """Test case for del_course_by_id

        delete a course by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses/{course_id}'.format(course_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_courses(self):
        """Test case for get_all_courses

        show all courses
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_course_by_id(self):
        """Test case for get_course_by_id

        Show detail a course by id
        """
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses/{course_id}'.format(course_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_course(self):
        """Test case for update_course

        method to update
        """
        body = Courses()
        response = self.client.open(
            '/phuthien007/ManagementStudent/1.0.0/api/courses',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
