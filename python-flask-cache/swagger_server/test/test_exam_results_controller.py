# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exam_results import ExamResults  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExamResultsController(BaseTestCase):
    """ExamResultsController integration test stubs"""

    def test_add_exam_result(self):
        """Test case for add_exam_result

        add a exam_result
        """
        body = ExamResults()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exam_results',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_exam_result_by_id(self):
        """Test case for del_exam_result_by_id

        delete a exam_result by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exam_results/{exam_result_id}'.format(exam_result_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_exam_results(self):
        """Test case for get_all_exam_results

        show all exam_results
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exam_results',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam_result_by_id(self):
        """Test case for get_exam_result_by_id

        Show detail a exam_results by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exam_results/{exam_result_id}'.format(exam_result_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_exam_result(self):
        """Test case for update_exam_result

        method to update
        """
        body = ExamResults()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/exam_results',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
