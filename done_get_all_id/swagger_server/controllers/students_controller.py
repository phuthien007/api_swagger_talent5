import connexion
import six

from swagger_server.models.students import Students  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*


def add_student(body):  # noqa: E501
    """add a student

    method to add a student # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Students
    """
    if connexion.request.is_json:
        body = Students.from_dict(connexion.request.get_json())  # noqa: E501
    #create a new instant student
    new_student = Students_instants(address=body.address,birthday=body.birthday,email=body.email,facebook=body.facebook,full_name=body.full_name,note=body.note,phone=body.phone)
    # use func add_data is defined by utils.py
    add_data(new_student)
    return body


def del_student_by_id(student_id):  # noqa: E501
    """delete a student by id

    method to delete a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: None
    """
    try:
        current_student= session.query(Students_instants).filter(Students_instants.student_id == student_id).first()
        current_exam_results= session.query(Exam_results_instants).filter(Exam_results_instants.student_id == current_student.student_id).first()
        current_registration= session.query(Registrations_instants).filter(Registrations_instants.student_id == current_student.student_id).first()
        if current_student == None:
            return "404 - Not Found"
        elif current_exam_results != None:
            return f"400 - bad request ( table exam_results)"
        elif current_registration != None:
            return "400 - bad request ( table registrations) "
        else:
            delete_data(current_student)
            session.commit()
            return "success"
    except Exception:
        session.rollback()
        return "404 not found"
    finally:
        session.close()


def get_all_students():  # noqa: E501
    """show all students

    method to get data student # noqa: E501


    :rtype: List[Students]
    """
    rows = get_all_data(Students_instants)
    if rows == None:
        return "Not data"
    data=[]
    for item in rows:
        data.append({
            "address": item.address,
            "birthday": item.birthday,
            "create_date": item.create_date,
            "email": item.email,
            "facebook": item.facebook,
            "full_name": item.full_name,
            "note": item.note,
            "phone": item.phone,
            "student_id": item.student_id
        })
    return data


def get_student_by_id(student_id):  # noqa: E501
    """Show detail a student by id

    method to show info a student by student_id # noqa: E501

    :param student_id: fill in id a student
    :type student_id: int

    :rtype: Students
    """
    item= session.query(Students_instants).filter(Students_instants.student_id == student_id).first()
    if item == None:
        return "Not data"
    data= {
            "address": item.address,
            "birthday": item.birthday,
            "create_date": item.create_date,
            "email": item.email,
            "facebook": item.facebook,
            "full_name": item.full_name,
            "note": item.note,
            "phone": item.phone,
            "student_id": item.student_id
        }
    return data


def update_student(body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Students.from_dict(connexion.request.get_json())][0]  # noqa: E501
    try:
        current_student= session.query(Students_instants).filter(Students_instants.student_id == body.student_id).first()
        current_student.address= body.address,
        current_student.birthday= body.birthday,
        current_student.create_date= body.create_date,
        current_student.email=body.email,
        current_student.facebook= body.facebook,
        current_student.full_name= body.full_name,
        current_student.note= body.note,
        current_student.phone= body.phone
        session.commit()
        return body
    except Exception:
        return "fail"
        session.rollback()  
    finally:
        session.close()
