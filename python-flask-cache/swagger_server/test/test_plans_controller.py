# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.plans import Plans  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlansController(BaseTestCase):
    """PlansController integration test stubs"""

    def test_add_plan(self):
        """Test case for add_plan

        add a plan
        """
        body = Plans()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/plans',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_plan_by_id(self):
        """Test case for del_plan_by_id

        delete a plan by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/plans/{plan_id}'.format(plan_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_plans(self):
        """Test case for get_all_plans

        show all plans
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/plans',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_plan_by_id(self):
        """Test case for get_plan_by_id

        Show detail a plan by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/plans/{plan_id}'.format(plan_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_plan(self):
        """Test case for update_plan

        method to update
        """
        body = Plans()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/plans',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
