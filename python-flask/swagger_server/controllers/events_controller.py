import connexion
import six

from swagger_server.controllers import classes_controller
from swagger_server.models.events import Events  # noqa: E501
from swagger_server import util
from swagger_server.controllers.utils import *
from swagger_server.controllers import *
from swagger_server.controllers.users_controller import *
from sqlalchemy import or_,and_
from flask import jsonify, make_response
from swagger_server.controllers import*
@token_required
def add_event(f,body):  # noqa: E501

    """add a event

    method to add a event # noqa: E501

    :param body: create event object
    :type body: dict | bytes

    :rtype: Events
    """
    if check_authorization(f,"can_add_event") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    if connexion.request.is_json:
        body = Events.from_dict(connexion.request.get_json()) # noqa: E501
    try:
        item= session.query(Events_instants).filter(and_(Events_instants.name==body.name, Events_instants.create_date==body.create_date, Events_instants.happen_date==body.happen_date, Events_instants.status==body.status, Events_instants.class_id==body._class.id )).first() 
        if item:
            return jsonify({"message":"event is exist!!!"}), 400
        new_event = Events_instants(name=body.name, create_date=body.create_date,happen_date=body.happen_date,status=body.status,class_id=body._class.id )
        current_class= session.query(Classes_instants).filter(Classes_instants.id == new_event.class_id).first()
        if current_class == None :
            return "400 - bad request (class object is not exsist"
        add_data(new_event)
        item= session.query(Events_instants).filter(and_(Events_instants.name==body.name, Events_instants.create_date==body.create_date, Events_instants.happen_date==body.happen_date, Events_instants.status==body.status, Events_instants.class_id==body._class.id )).first() 
        # data_course is used contain data of course has course_id = item.course_id
        return get_event_by_id(item.id)
    except Exception as e:
        return jsonify({"message":f"{e}"}),400


@token_required
def del_event_by_id(f,event_id):  # noqa: E501
    """delete a event by id

    method to delete a event by event_id # noqa: E501

    :param event_id: fill in id a event
    :type event_id: int

    :rtype: None
    """
    if check_authorization(f,"can_delete_event_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    choose_event= session.query(Events_instants).filter(Events_instants.id == event_id).first()
    if not choose_event:
        return jsonify({"message":"ID Unknown"}),404
    delete_data(choose_event)
    return "success"

@token_required
def get_all_events(f,key_word=None, page_num=0, records_per_page=20):  # noqa: E501
    
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
    if check_authorization(f,"can_view_all_events") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    rows, number_of_records= get_all_data(Events_instants)
    if rows == None:
        return errors["400"][0],errors["400"][1]
    if key_word:
        try:
            key_word=int(key_word)
            c= classes_controller.get_classes_by_id(key_word)
            rows = rows.filter(or_(Events_instants.class_id == c['id']))                     
        except:
            rows = rows.filter(or_(Events_instants.name.like(f'%{key_word}%'),
                                Events_instants.status.like(f'%{key_word}%')))   
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
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data.append({
            "class": data_class,
            "create_date": "2000-01-23T04:56:07+00:00",
            "id": item.id,
            "happen_date": item.happen_date,
            "name": item.name,
            "status": item.status
        })
    return data,200,{"total_of_records":number_of_records,"total_of_pages": total_pages}

@token_required
def get_event_by_id(f,event_id):  # noqa: E501
    """Show detail a event by id

    method to show info a event by event_id # noqa: E501

    :param event_id: fill in id a event
    :type event_id: int

    :rtype: Events
    """
    if check_authorization(f,"can_view_event_by_id") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    # orm api session
    try:
        item= session.query(Events_instants).filter(Events_instants.id == event_id).first() 
       
        if item == None:
            return  errors["404"][0],errors["404"][1]  
        data_class= classes_controller.get_classes_by_id(item.class_id)
        data={
            "class": data_class,
            "create_date": "2000-01-23T04:56:07+00:00",
            "id": item.id,
            "happen_date": item.happen_date,
            "name": item.name,
            "status": item.status
        }
        return data
    except Exception as e:
        print(e)
        return jsonify({"message":"not found"}),404
@token_required
def update_event(f,body):  # noqa: E501
    if check_authorization(f,"can_update_event") == False:
        return jsonify({"message":"the user dont has permision to request"}), 400
    
    """method to update

     # noqa: E501

    :param body: update event object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Events.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        current_event= session.query(Events_instants).filter(Events_instants.id == body.id).first()
        current_event.class_id= body._class.id,
        current_event.happen_date= body.happen_date,
        current_event.name= body.name,
        current_event.status= body.status,
        session.commit()
        return body
    except Exception as e:
        session.rollback()
        return jsonify({"message":f"{e}"}),400
    finally:
        session.close()