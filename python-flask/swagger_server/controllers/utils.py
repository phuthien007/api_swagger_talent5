from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.automap import automap_base
from functools import lru_cache
from swagger_server.models import *
import logging
from datetime import timedelta
import redis
# logging.basicConfig(filename='check.log', format='%(asctime)s %(levelname)s %(name)s: %(message)s')
engine = create_engine('postgresql://postgres:Thienphu1@localhost:5432/ManagementStudents', hide_parameters=True,
                       echo=False, query_cache_size=500)
Session = sessionmaker()
# config engine with session api
Session.configure(bind=engine)
session = Session()
Base = automap_base()
Base.prepare(engine, reflect=True)
# instant of table Teachers
Teachers_instants = Base.classes.teachers
# instant of table Courses
Courses_instants = Base.classes.courses
# instant of table Classes
Classes_instants = Base.classes.classes
# instant of table students
Students_instants = Base.classes.students
# instant of table events
Events_instants = Base.classes.events
# instant of table exam_results
Exam_results_instants = Base.classes.exam_results
# instant of table registrations
Registrations_instants = Base.classes.registrations
# instant of table exams
Exams_instants = Base.classes.exams
# instant of table plan
Plans_instants = Base.classes.plans
# instant of table user
Users_instants = Base.classes.users

role1 = Base.classes.authorization_each_role
role2 = Base.classes.authorization_each_author

#config redis server
redis_client= redis.Redis(host='localhost',port=6379,db=0) 

# get data

# count all record
# func to gen authorization for each role

def get_permis_each_role(role, per_id):
    role = role.strip()
    res = redis_client.get(f'res_{role}_{per_id}')
    # print(res)
    if res is None:
        res = session.query(role1).filter(and_(role1.role_name == role, role1.per_id == per_id)).first()
        if res == None or res == '':
            return None
        redis_client.psetex(f'res_{role}_{per_id}',timedelta(minutes=5),'true')
        # print(redis_client.get(f'res_{role}_{per_id}'))
        # res = redis_client.get(f'res_{role}_{per_id}')
        # print('day: ',res)
    # print(res)
    return res


# func to gen authorization for each user
def get_permis_each_author(user_id, per_id):
    res = redis_client.get(f'permis_{user_id}_{per_id}')
    if res is None:
        res = session.query(role2).filter(and_(role2.user_id == user_id, role2.per_id == per_id)).first()
        if res == None or res == '':
            return None
        redis_client.get(f'permis_{user_id}_{per_id}',timedelta(minutes=5),'true')
    return res


# get id in permis
def get_per_id(permis):
    with engine.begin() as conn:
        res = list(conn.execute(f"SELECT id FROM permistions WHERE per_name = '{permis}' ").fetchone())[0]
        if not res:
            return None
        return res


# get all data
def get_all_data(obj):
    
    rows = session.query(obj)
    number_of_rows = session.query(obj).count()

    return rows, number_of_rows

# func to add a instant object into table object through orm api session
def add_data(obj):
    try:
        session.add(obj)
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()


def delete_data(obj):
    try:
        session.delete(obj)
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()


# list of error
errors = {
    "404": [{
        "detail": "ID Unknown",
        "status": 404,
        "title": "Not Found",
        "type": "about:blank"
    }, 404],
    "400": [{
        "detail": "The server could not understand the request due to invalid syntax",
        "status": 400,
        "title": "Bad Request",
        "type": "about:blank"
    }, 400],
    "401": [{
        "detail": "the client must authenticate itself to get the requested response",
        "status": 401,
        "title": "Unauthorized",
        "type": "about:blank"
    }, 401],
    "405": [{
        "detail": "The method request  has been disabled and cannot be used",
        "status": 405,
        "title": "Method not allow",
        "type": "about:blank"
    }, 405],
    "403": [{
        "detail": "The client does not have access rights to the content",
        "status": 403,
        "title": "Forbidden",
        "type": "about:blank"
    }, 403]

}
