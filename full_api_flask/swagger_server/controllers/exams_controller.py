import connexion
import six
from flask import jsonify, make_response
from swagger_server.models.events import Events  # noqa: E501
from swagger_server.models.exams import Exams  # noqa: E501
from swagger_server import util
from swagger_server.controllers.users_controller import *
from swagger_server.controllers.utils import*
from swagger_server.controllers import*
from sqlalchemy import and_, or_

@token_required
def add_exam(f,body):  # noqa: E501
    
    """add a exam

    method to add a exam # noqa: E501

    :param body: create exam object
    :type body: dict | bytes

    :rtype: Exams
    """
    if connexion.request.is_json:
        body = Exams.from_dict(connexion.request.get_json())  # noqa: E501
    
    if not body:
        return jsonify({"message":"data not exist"}),404
    item= session.query(Exams_instants).filter(Exams_instants.course_id == body.course_id.course_id, Exams_instants.name == body.name).first()
    if item:
        return jsonify({"message":"the exam is exist"}),400
    
    try:
        data_course= courses_controller.get_course_by_id(body.course_id.course_id)
        new_exam= Exams_instants(course_id = body.course_id.course_id, name= body.name)
        add_data(new_exam)
        item= session.query(Exams_instants).filter(Exams_instants.course_id == body.course_id.course_id, Exams_instants.name == body.name).first()
        if not item:
            return errors["400"][0],errors["400"][1]
        return jsonify({
            "course_id":data_course,
            "name":item.name,
            "plan_id":item.exam_id
        })
    except Exception as e:
        
        return jsonify({"message":f"{e}"}),400

@token_required
def del_exam_by_id(f,exam_id):  # noqa: E501
    
    """delete a exam by id

    method to delete a exam by exam_id # noqa: E501

    :param exam_id: fill in id a exam
    :type exam_id: int

    :rtype: None
    """
    permis= get_per_id("can_delete_exam_by_id")
    permit = get_permis((f.role_id), (permis))
    if permis:
        return jsonify({"message":"the user dont has permision to request"}), 400 
    item= session.query(Exams_instants).filter(Exams_instants.exam_id == exam_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    delete_data(item)
    return 'success'

@token_required
def get_all_exams(f, key_word=None, page_num=None, records_per_page=None):  # noqa: E501
    """show all exams

    method to get data exam # noqa: E501

    :param key_word: you can fill key word you want to search
    :type key_word: str
    :param page_num: number of page
    :type page_num: float
    :param records_per_page: number record in a page
    :type records_per_page: float

    :rtype: List[Exams]
    """
    permis= get_per_id("can_view_all_exams")
    permit = get_permis((f.role_id), (permis))
    if permis:
        return jsonify({"message":"the user dont has permision to request"}), 400
    rows= get_all_data(Exams_instants)
    if not rows:
        return jsonify({"message":"not data"}),400
    if key_word:
        try:
            key_word = int(key_word)
            rows=rows.filter(Exams_instants.course_id == key_word)
        except:
            rows=rows.filter((Exams_instants.name.like(f"%{key_word}%")))
    if records_per_page:
        rows=rows.limit(records_per_page)
        if page_num:
            rows= rows.offset(records_per_page* page_num)
    data=[]
    for item in rows:
        data_course= courses_controller.get_course_by_id(item.course_id)
        data.append({
            "course_id": data_course,
            "name":item.name,
            "exam_id": item.exam_id
        })
    return data

@token_required
def get_exam_by_id(f,exam_id):  # noqa: E501
    
    """Show detail a exam by id

    method to show info a exam by exam_id # noqa: E501

    :param exam_id: fill in id a event
    :type exam_id: int

    :rtype: Exams
    """
    permis= get_per_id("can_view_exam_by_id")
    permit = get_permis((f.role_id), (permis))
    if permis:
        return jsonify({"message":"the user dont has permision to request"}), 400
    item= session.query(Exams_instants).filter(Exams_instants.exam_id == exam_id).first()
    if item == None:
        return  errors["404"][0],errors["404"][1]
    data_course= courses_controller.get_course_by_id(item.course_id)
    data={
        "course_id": data_course,
        "name":item.name,
        "exam_id": item.exam_id
    }
    return data

@token_required
def update_exam(f,body):  # noqa: E501
    
    """method to update

     # noqa: E501

    :param body: update exam object
    :type body: dict | bytes

    :rtype: None
    """
    permis= get_per_id("can_update_exam")
    permit = get_permis((f.role_id), (permis))
    if permis:
        return jsonify({"message":"the user dont has permision to request"}), 400
    if connexion.request.is_json:
        body = Exams.from_dict(connexion.request.get_json()) # noqa: E501
   
    if not body or not body.exam_id :
        return jsonify({"message":"missing data" }),400
    try:
        data_course= courses_controller.get_course_by_id(body.course_id.course_id)
      
        item= session.query(Exams_instants).filter(Exams_instants.exam_id == body.exam_id).first()
  
        item.course_id = data_course['course_id']
        item.name = body.name
        session.commit()
        return body
    except Exception :
        return jsonify({"message":"bad request"}), 400
