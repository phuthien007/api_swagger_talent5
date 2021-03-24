# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassesController(BaseTestCase):
    """ClassesController integration test stubs"""

    def test_add_class(self):
        """Test case for add_class

        add a class
        """
        body = [Classes()]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/classes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_class_by_i(self):
        """Test case for del_class_by_i

        delete a class by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/classes/{class_id}'.format(class_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_classes(self):
        """Test case for get_all_classes

        show all classes
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/classes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_classes_by_id(self):
        """Test case for get_classes_by_id

        Show detail a class by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/classes/{class_id}'.format(class_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_class(self):
        """Test case for update_class

        method to update
        """
        body = [Classes()]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/classes',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
