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
    if check_authorization(f,"can_add_exam_result") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body._class or not body.exam or not body.student:
        return jsonify({"message":"missing value"}), 400
    try:
        
        data_class = classes_controller.get_classes_by_id(body._class.id)
        data_student= students_controller.get_student_by_id(body.student.id)
        data_exam= exams_controller.get_exam_by_id(body.exam.id)
        note= body.note
        score= body.score
        result_date= body.result_date
        item= session.query(Exam_results_instants).filter(and_(Exam_results_instants.class_id == body._class.id, Exam_results_instants.student_id == body.student.id, Exam_results_instants.exam_id == body.exam.id, Exam_results_instants.score == score, Exam_results_instants.note == note,Exam_results_instants.result_date == result_date)).first()
        if item:
            return jsonify({"message":"the exam_result is exist"}), 400
        new_item= Exam_results_instants(class_id =body._class.id, student_id = body.student.id, exam_id = body.exam.id,score = body.score, note = body.note,result_date = body.result_date)
        add_data(new_item)
        item= session.query(Exam_results_instants).filter(and_(Exam_results_instants.class_id == body._class.id, Exam_results_instants.student_id == body.student.id, Exam_results_instants.exam_id == body.exam.id, Exam_results_instants.score == score, Exam_results_instants.note == note,Exam_results_instants.result_date == result_date)).first()
        if item == None:
            return  errors["404"][0],errors["404"][1]
        return get_exam_result_by_id(item.id)
    except Exception as e:
        return jsonify({"message":"Bad request"}), 400

@token_required
def del_exam_result_by_id(f,exam_result_id):  # noqa: E501
    
    """delete a exam_result by id

    method to delete a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result_id
    :type exam_result_id: int

    :rtype: None
    """
    if check_authorization(f,"can_delete_exam_result_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    item= session.query(Exam_results_instants).filter(Exam_results_instants.id == exam_result_id).first()
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
    if check_authorization(f,"can_view_all_exam_results") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    rows, number_of_records= get_all_data(Exam_results_instants)
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
    total_pages= number_of_records//20 + 1
    records_per_page = 0 if records_per_page <0 else records_per_page
    if records_per_page>=0:
        if page_num>=0:
            rows= rows.offset(records_per_page* page_num)
            if number_of_records > records_per_page and int(records_per_page) != 20:
                number_of_records = int(records_per_page)
            total_pages= number_of_records//20 + 1
            if records_per_page > 20:
                records_per_page = 20
            rows= rows.limit(records_per_page)
    data=[]
    for item in rows:
        data_student= students_controller.get_student_by_id(item.student_id)
        data_exam= exams_controller.get_exam_by_id(item.exam_id)
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data.append({
            "id": item.id,
            "student":data_student,
            "exam":data_exam,
            "score": item.score,
            "class": data_class,
            "note": item.note,
            "result_date": item.result_date
        })
    return data,200,{"total_of_records":number_of_records,"total_of_pages": total_pages}

@token_required
def get_exam_result_by_id(f,exam_result_id):  # noqa: E501
    """Show detail a exam_results by id

    method to show info a exam_result by exam_result_id # noqa: E501

    :param exam_result_id: fill in id a exam_result
    :type exam_result_id: int

    :rtype: ExamResults
    """
    if check_authorization(f,"can_view_exam_result_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    item= session.query(Exam_results_instants).filter(Exam_results_instants.id == exam_result_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    data_student= students_controller.get_student_by_id(item.student_id)
    data_exam= exams_controller.get_exam_by_id(item.exam_id)
    data_class= classes_controller.get_classes_by_id(item.class_id)
    data={
        "id": item.id,
        "student":data_student,
        "exam":data_exam,
        "score": item.score,
        "class": data_class,
        "note": item.note,
        "result_date":item.result_date
    }
    return data

@token_required
def update_exam_result(f,body):  # noqa: E501
    if check_authorization(f,"can_update_exam_result") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    """method to update

     # noqa: E501

    :param body: update exam_result object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ExamResults.from_dict(connexion.request.get_json())  # noqa: E501
    if not body or not body._class or not body.exam or not body.student or not body.id:
        return jsonify({"message":"missing value"}), 400
    try:
        data_class = classes_controller.get_classes_by_id(body._class.id)
        data_student=  students_controller.get_student_by_id(body.student.id)
        data_exam=  exams_controller.get_exam_by_id(body.exam.id)
        note= body.note
        score= body.score
        result_date= body.result_date
        item= session.query(Exam_results_instants).filter(Exam_results_instants.id == body.id).first()
        if not item:
            return jsonify({"message":"the exam_result is exist"}), 400
        item.student_id=  body.student.id
        item.exam_id= body.exam.id
        item.class_id=  body._class.id
        item.score= score
        item.note = note
        item.result_date= result_date
        return get_exam_result_by_id(item.id)
    except Exception as e:
        return jsonify({"message":"Bad request"}), 400