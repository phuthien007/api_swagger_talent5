import connexion
import six
import json
from swagger_server.controllers.users_controller import*
from swagger_server.models.classes import Classes  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import*
from swagger_server.controllers import teachers_controller, courses_controller
from sqlalchemy import or_,and_
from swagger_server.controllers import*
#update date using orm api session
@token_required
def add_class(f,body):  # noqa: E501
    """add a class

    method to add a class # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Classes
    """
    if check_authorization(f,"can_add_class") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    if connexion.request.is_json:
        body = (connexion.request.get_json())  # noqa: E501
    # create a new instant class
    try:
        item= session.query(Classes_instants).filter(and_(Classes_instants.name==body.get('name'), Classes_instants.start_date==body.get('start_date'), Classes_instants.end_date==body.get('end_date'), Classes_instants.status==body.get('status'), Classes_instants.course_id==body.get('course').get('id') , Classes_instants.teacher_id==body.get('teacher').get('id'))).first() 
        if item:
            return jsonify({"message":"the class is exist"}),400
        new_class = Classes_instants(name=body.get('name'), start_date=body.get('start_date'),end_date=body.get('end_date'),status=body.get('status'),course_id=body.get('course').get('id') ,teacher_id=body.get('teacher').get('id'))
        current_course= session.query(Courses_instants).filter(Courses_instants.id == new_class.course_id).first()
        current_teacher= session.query(Teachers_instants).filter(Teachers_instants.id == new_class.teacher_id).first()
        # use func add_data is defined by utils.py
        if current_course == None or current_teacher ==None:
            return "400 - bad request (course object or teacher object is not exsist"
        add_data(new_class)
        item= session.query(Classes_instants).filter(and_(Classes_instants.name==body.get('name'), Classes_instants.start_date==body.get('start_date'), Classes_instants.end_date==body.get('end_date'), Classes_instants.status==body.get('status'), Classes_instants.course_id==body.get('course').get('id') , Classes_instants.teacher_id==body.get('teacher').get('id'))).first() 
        # data_course is used contain data of course has course_id = item.course_id
        data_course= courses_controller.get_course_by_id(item.course_id)
        # data_teacher is used contain data of course has teacher_id = item.teacher_id
        data_teacher= teachers_controller.get_teacher_by_id(item.teacher_id)
        data ={
                "id": item.id,
                "course": data_course,
                "end_date": item.end_date,
                "name": item.name,
                "start_date": item.start_date,
                "status": item.status,
                "teacher":data_teacher
            }
        return data
    except Exception as e :
        print(e)
        return errors["400"][0],errors["400"][1]

@token_required
def del_class_by_id(f,class_id):  # noqa: E501
    """delete a class by id

    method to delete a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: None
    """
    if check_authorization(f,"can_delete_class_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    try:
        current_class= session.query(Classes_instants).filter(Classes_instants.id == class_id).first()
        current_exam_result= session.query(Exam_results_instants).filter(Exam_results_instants.class_id == class_id).first()
        current_registration= session.query(Registrations_instants).filter(Registrations_instants.class_id == class_id).first()
        if current_class == None:
            return "404 - Not Found"
        elif current_exam_result != None:
            return "400 - bad request ( table exam_results)"
        elif current_registration != None:
            return "400 - bad request ( table registrations) "
        else:
            delete_data(current_class)
            session.commit()
            return "success"
    except Exception:
        session.rollback()
        return errors["405"][0],errors["405"][1]
    finally:
        session.close()

# method to get data from database and show all
@token_required
def get_all_classes(f,type_name=None, key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    """show all classes

    method to get data course # noqa: E501
    :rtype: List[Classes]
    """
    if check_authorization(f,"can_view_all_classes") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    rows, number_of_records = get_all_data(Classes_instants)
    if rows == None:
        return errors["400"][0],errors["400"][1]
    if key_word:
        try:
            key_word=int(key_word)
            c= courses_controller.get_course_by_id(key_word)
            t= teachers_controller.get_teacher_by_id(key_word)
            rows = rows.filter(or_(Classes_instants.course_id == c['id'],Classes_instants.teacher_id == t['id']))                     
        except:
            rows = rows.filter(or_(Classes_instants.name.like(f'%{key_word}%'),
                                Classes_instants.status.like(f'%{key_word}%')))    
        
    total_pages= number_of_records//20 + 1
    records_per_page = 0 if records_per_page <0 else records_per_page
    if records_per_page>=0:
        if page_num>=0:
            rows= rows.offset(records_per_page* page_num)
            if number_of_records > records_per_page and int(records_per_page) != 20:
                number_of_records = int(records_per_page)
            total_pages= number_of_records//20 + 1
            if records_per_page > 20 :
                records_per_page = 20
            rows= rows.limit(records_per_page)
    data=[]
    for item in rows:
        data_course= courses_controller.get_course_by_id(item.course_id)
        data_teacher= teachers_controller.get_teacher_by_id(item.teacher_id)
        data.append({
            "id": item.id,
            "course": data_course,
            "end_date": item.end_date,
            "name": item.name,
            "start_date": item.start_date,
            "status": item.status,
            "teacher": data_teacher
        })
    return data,200,{"total_of_records":number_of_records,"total_of_pages": total_pages}

@token_required
def get_classes_by_id(f,class_id):  # noqa: E501
    """Show detail a class by id

    method to show info a class by class_id # noqa: E501

    :param class_id: fill in id a class
    :type class_id: int

    :rtype: Classes
    """
    if check_authorization(f,"can_view_class_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    
    # orm api session
    item= session.query(Classes_instants).filter(Classes_instants.id == class_id).first() 
    if item == None:
        return  errors["404"][0],errors["404"][1]
    # data_course is used contain data of course has course_id = item.course_id
    data_course= courses_controller.get_course_by_id(item.course_id)
    # data_teacher is used contain data of course has teacher_id = item.teacher_id
    data_teacher= teachers_controller.get_teacher_by_id(item.teacher_id)
    data ={
            "id": item.id,
            "course":data_course,
            "end_date": item.end_date,
            "name": item.name,
            "start_date": item.start_date,
            "status": item.status,
            "teacher": data_teacher
        }
    return data

@token_required
def update_class(f,body):  # noqa: E501
    """method to update

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if check_authorization(f,"can_update_class") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    if connexion.request.is_json:
        body = [(connexion.request.get_json())[0]][0] # noqa: E501
    try:
        current_class= session.query(Classes_instants).filter(Classes_instants.id == body.get('id')).first()
        current_class.course_id= body.get('course').get('id'),
        current_class.end_date= body.get('end_date'),
        current_class.name= body.get('name'),
        current_class.start_date=body.get('start_date'),
        current_class.status= body.get('status'),
        current_class.teacher_id= body.get('teacher').get('id')
        session.commit()
        return body
    except Exception as e:
        session.rollback()
        return errors["404"][0],errors["404"][1]  
    finally:
        session.close()