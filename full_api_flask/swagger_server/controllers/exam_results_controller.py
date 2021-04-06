import connexion
import six
from flask import jsonify
from sqlalchemy import or_, and_

from swagger_server.controllers import students_controller, exams_controller, classes_controller
from swagger_server.models.exam_results import ExamResults  # noqa: E501
from swagger_server import util
from swagger_server.controllers.users_controller import*
from swagger_server.controllers.utils import*
from swagger_server.controllers import*

@token_required
def add_exam_result(f,body):  # noqa: E501
    """add a exam_result

    method to add a exam_result # noqa: E501

    :param body: create exam_result object
    :type body: dict | bytes

    :rtype: ExamResults
    """
    permis = get_per_id("can_add_exam_result")
    permis = get_permis((f.role_id), (permis))
    if not permis:
        return jsonify({"message": "the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body.class_id or not body.exam_id or not body.student_id:
        return jsonify({"message":"missing value"}), 400
    try:
        data_class = session.query(Classes_instants).filter(Classes_instants.class_id == body.class_id.class_id).first()
        data_student= session.query(Students_instants).filter(Students_instants.student_id == body.student_id.student_id).first()
        data_exam= session.query(Exams_instants).filter(Exams_instants.exam_id == body.exam_id.exam_id).first()
        note= body.note
        score= body.score
        result_date= body.result_date
        item= session.query(Exam_results_instants).filter(and_(Exam_results_instants.class_id == body.class_id.class_id, Exam_results_instants.student_id == body.student_id.student_id, Exam_results_instants.exam_id == body.exam_id.exam_id, Exam_results_instants.score == score, Exam_results_instants.note == note,Exam_results_instants.result_date == result_date)).first()
        if item:
            return jsonify({"message":"the exam_result is exist"}), 400
        new_item= Exam_results_instants(class_id = body.class_id.class_id, student_id = body.student_id.student_id, exam_id = body.exam_id.exam_id,score = body.score, note = body.note,result_date = body.result_date)
        add_data(new_item)
        item= session.query(Exam_results_instants).filter(and_(Exam_results_instants.class_id == body.class_id.class_id, Exam_results_instants.student_id == body.student_id.student_id, Exam_results_instants.exam_id == body.exam_id.exam_id, Exam_results_instants.score == body.score, Exam_results_instants.note == body.note, Exam_results_instants.result_date == result_date)).first()
        if item == None:
            return  errors["404"][0],errors["404"][1]
        data_student= students_controller.get_student_by_id(item.student_id)
        data_exam= exams_controller.get_exam_by_id(item.exam_id)
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data={
            "exam_result_id": item.exam_result_id,
            "student_id":data_student,
            "exam_id":data_exam,
            "score": item.score,
            "class_id": data_class,
            "note": item.note,
            "result_date": item.result_date
        }
        return data
    except Exception as e:
        print(e) 
        return jsonify({"message":"Bad request"}), 400

@token_required
def del_exam_result_by_id(f,exam_result_id):  # noqa: E501
    
    """delete a exam_result by id

    method to delete a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result_id
    :type exam_result_id: int

    :rtype: None
    """
    permis= get_per_id("can_delete_exam_result_by_id")
    permis = get_permis((f.role_id), (permis))
    if not permis:
        return jsonify({"message":"the user dont has permision to request"}), 400
    item= session.query(Exam_results_instants).filter(Exam_results_instants.exam_result_id == exam_result_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    delete_data(item)
    return 'success'

@token_required
def get_all_exam_results(f,key_word=None, page_num=0, records_per_page=20):  # noqa: E501
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
    permis = get_per_id("can_view_all_exam_results")
    permis = get_permis((f.role_id), (permis))
    if not permis:
        return jsonify({"message": "the user dont has permision to request"}), 400
    rows= get_all_data(Exam_results_instants)
    if not rows:
        return jsonify
    if key_word:
        try:
            key_word= int(key_word)
            rows= rows.filter(or_(Exam_results_instants.student_id == key_word, 
                                 Exam_results_instants.exam_id == key_word, 
                                 Exam_results_instants.class_id == key_word, 
                                 Exam_results_instants.score == key_word))
        except:
            rows= rows.filter(Exam_results_instants.note.like(f"%{key_word}%"))
    if records_per_page>=0:
        rows= rows.limit(records_per_page)
        if page_num>=0:
            rows= rows.offset(records_per_page  * page_num)
    data=[]
    for item in rows:
        data_student= students_controller.get_student_by_id(item.student_id)
        data_exam= exams_controller.get_exam_by_id(item.exam_id)
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data.append({
            "exam_result_id": item.exam_result_id,
            "student_id":data_student,
            "exam_id":data_exam,
            "score": item.score,
            "class_id": data_class,
            "note": item.note,
            "result_date": item.result_date
        })
    return data

@token_required
def get_exam_result_by_id(f,exam_result_id):  # noqa: E501
    """Show detail a exam_results by id

    method to show info a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result
    :type exam_result_id: int

    :rtype: ExamResults
    """
    permis= get_per_id("can_view_exam_result_by_id")
    permis = get_permis((f.role_id), (permis))
    if not permis:
        return jsonify({"message":"the user dont has permision to request"}), 400
    item= session.query(Exam_results_instants).filter(Exam_results_instants.exam_result_id == exam_result_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    data_student= students_controller.get_student_by_id(item.student_id)
    data_exam= exams_controller.get_exam_by_id(item.exam_id)
    data_class= classes_controller.get_classes_by_id(item.class_id)
    data={
        "exam_result_id": item.exam_result_id,
        "student_id":data_student,
        "exam_id":data_exam,
        "score": item.score,
        "class_id": data_class,
        "note": item.note,
        "result_date":item.result_date
    }
    return data

@token_required
def update_exam_result(f,body):  # noqa: E501
    permis = get_per_id("can_update_exam_result")
    permis = get_permis((f.role_id), (permis))
    if not permis:
        return jsonify({"message": "the user dont has permision to request"}), 400
    """method to update

     # noqa: E501

    :param body: update exam_result object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body.class_id or not body.exam_id or not body.student_id or not body.exam_result_id:
        return jsonify({"message":"missing value"}), 400
    try:
        data_class = classes_controller.get_classes_by_id(body.class_id.class_id)
        data_student=  students_controller.get_student_by_id(body.student_id.student_id)
        data_exam=  exams_controller.get_exam_by_id(body.exam_id.exam_id)
        note= body.note
        score= body.score
        result_date= body.result_date
        item= session.query(Exam_results_instants).filter(Exam_results_instants.exam_result_id == body.exam_result_id).first()
        if not item:
            return jsonify({"message":"the exam_result is exist"}), 400
        item.student_id=  body.student_id.student_id
        item.exam_id= body.exam_id.exam_id
        item.class_id=  body.class_id.class_id
        item.score= score
        item.note = note
        item.result_date= result_date
        data={
            "exam_result_id": item.exam_result_id,
            "student_id":data_student,
            "exam_id":data_exam,
            "score": item.score,
            "class_id": data_class,
            "note": item.note,
            "result_date": item.result_date
        }
        return data
    except Exception as e:
        print(e) 
        return jsonify({"message":"Bad request"}), 400