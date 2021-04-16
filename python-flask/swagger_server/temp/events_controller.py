import connexion
import six

from swagger_server.models.events import Events  # noqa: E501
from swagger_server import util


def add_event(body):  # noqa: E501
    """add a event

    method to add a event # noqa: E501

    :param body: create event object
    :type body: dict | bytes

    :rtype: Events
    """
    if connexion.request.is_json:
        body = Events.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_event_by_id(event_id):  # noqa: E501
    """delete a event by id

    method to delete a event by event_id # noqa: E501

    :param event_id: fill in id a event
    :type event_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_events(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all events

    method to get data event # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Events]
    """
    return 'do some magic!'


def get_event_by_id(event_id):  # noqa: E501
    """Show detail a event by id

    method to show info a event by event_id # noqa: E501

    :param event_id: fill in id a event
    :type event_id: int

    :rtype: Events
    """
    return 'do some magic!'


def update_event(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update event object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Events.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
