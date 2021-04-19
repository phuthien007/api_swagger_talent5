# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.registrations import Registrations  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegistrationsController(BaseTestCase):
    """RegistrationsController integration test stubs"""

    def test_add_registration(self):
        """Test case for add_registration

        add a registrations
        """
        body = Registrations()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/registrations',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_registration_by_id(self):
        """Test case for del_registration_by_id

        delete a registration by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/registrations/{class_id}/{student_id}'.format(class_id=789, student_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_registrations(self):
        """Test case for get_all_registrations

        show all registrations
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/registrations',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_registration_by_id(self):
        """Test case for get_registration_by_id

        Show detail a registrations by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/registrations/{class_id}/{student_id}'.format(class_id=789, student_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_registration(self):
        """Test case for update_registration

        method to update
        """
        body = Registrations()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/registrations',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
