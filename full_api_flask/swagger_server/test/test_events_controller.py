# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.events import Events  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventsController(BaseTestCase):
    """EventsController integration test stubs"""

    def test_add_event(self):
        """Test case for add_event

        add a event
        """
        body = Events()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/events',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_event_by_id(self):
        """Test case for del_event_by_id

        delete a event by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/events/{event_id}'.format(event_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_events(self):
        """Test case for get_all_events

        show all events
        """
        query_string = [('key_word', 'key_word_example'),
                        ('page_num', 1.2),
                        ('records_per_page', 1.2)]
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/events',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Show detail a event by id
        """
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/events/{event_id}'.format(event_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_event(self):
        """Test case for update_event

        method to update
        """
        body = Events()
        response = self.client.open(
            '/phuthien007/test/1.0.0/api/events',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
