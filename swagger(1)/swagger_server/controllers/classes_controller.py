import connexion
import six

from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*

classes= "classes"

def add_class(body):  # noqa: E501
    """add a class

    method to add a class # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Classes
    """
    if connexion.request.is_json:
        body = Classes.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_class_by_id(class_id):  # noqa: E501
    """delete a class by id

    method to delete a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_classes():  # noqa: E501
    """show all classes

    method to get data course # noqa: E501


    :rtype: List[Classes]
    """
    rows = get_all_data(classes)
    if rows == None:
        return "Not data"
    data=[]
    for item in rows.fetchall():
        data_course= get_data_by_id("course",item[4])
        data_teacher= get_data_by_id("teacher",item[5])
        data.append({
            "class_id": item[0],
            "course_id": {
                "course_id": data_course[0],
                "create_date": data_course[3],
                "name": data_course[1],
                "type": data_course[2]
                },
            "end_date": item[3],
            "name": item[1],
            "start_date": item[2],
            "status": item[6],
            "teacher_id": {
                "address": data_teacher[4],
                "email": data_teacher[2],
                "full_name": data_teacher[1],
                "grade": data_teacher[5],
                "phone": data_teacher[3],
                "teacher_id": data_teacher[0]
                }
        })
    return data


def get_classes_by_id(class_id):  # noqa: E501
    """Show detail a class by id

    method to show info a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: Classes
    """
    with engine.begin() as conn:
        sql =f'''
            SELECT * FROM classes
            WHERE class_id = {class_id}
        '''
        row= conn.execute(sql).fetchone()
        item=row 
    if item == None or item =="":
        return "Not data"
    data_course= get_data_by_id("course",item[4])
    data_teacher= get_data_by_id("teacher",item[5])
    data={
        "class_id": item[0],
        "course_id": {
            "course_id": data_course[0],
            "create_date": data_course[3],
            "name": data_course[1],
            "type": data_course[2]
            },
        "end_date": item[3],
        "name": item[1],
        "start_date": item[2],
        "status": item[6],
        "teacher_id": {
            "address": data_teacher[4],
            "email": data_teacher[2],
            "full_name": data_teacher[1],
            "grade": data_teacher[5],
            "phone": data_teacher[3],
            "teacher_id": data_teacher[0]
            }
    }
    return data


def update_class(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Classes.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'