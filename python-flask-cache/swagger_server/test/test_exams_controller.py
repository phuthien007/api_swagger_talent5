# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exams import Exams  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExamsController(BaseTestCase):
    """ExamsController integration test stubs"""

    def test_add_exam(self):
        """Test case for add_exam

        add a exam
        """
        body = Exams()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exams',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_exam_by_id(self):
        """Test case for del_exam_by_id

        delete a exam by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exams/{exam_id}'.format(exam_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_exams(self):
        """Test case for get_all_exams

        show all exams
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exams',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam_by_id(self):
        """Test case for get_exam_by_id

        Show detail a exam by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exams/{exam_id}'.format(exam_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_exam(self):
        """Test case for update_exam

        method to update
        """
        body = Exams()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exams',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
