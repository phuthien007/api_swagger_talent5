import connexion
import six

from swagger_server.models.exam_results import ExamResults  # noqa: E501
from swagger_server import util


def add_exam_result(body):  # noqa: E501
    """add a exam_result

    method to add a exam_result # noqa: E501

    :param body: create exam_result object
    :type body: dict | bytes

    :rtype: ExamResults
    """
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_exam_result_by_id(exam_result_id):  # noqa: E501
    """delete a exam_result by id

    method to delete a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result_id
    :type exam_result_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_exam_results(key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all exam_results

    method to get data exam_results # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[ExamResults]
    """
    return 'do some magic!'


def get_exam_result_by_id(exam_result_id):  # noqa: E501
    """Show detail a exam_results by id

    method to show info a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result
    :type exam_result_id: int

    :rtype: ExamResults
    """
    return 'do some magic!'


def update_exam_result(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: update exam_result object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
