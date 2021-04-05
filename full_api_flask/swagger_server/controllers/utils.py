from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.automap import automap_base
from swagger_server.models import*
engine = create_engine('postgresql://postgres:Thienphu1@localhost:5432/ManagementStudents')

Session= sessionmaker()
#config engine with session api
Session.configure(bind= engine)
session= Session()
Base= automap_base()
Base.prepare(engine, reflect= True)
# instant of table Teachers
Teachers_instants= Base.classes.teachers
# instant of table Courses
Courses_instants= Base.classes.courses
# instant of table Classes
Classes_instants= Base.classes.classes
# instant of table students
Students_instants= Base.classes.students
# instant of table events
Events_instants= Base.classes.events
# instant of table exam_results
Exam_results_instants= Base.classes.exam_results
# instant of table registrations
Registrations_instants = Base.classes.registrations
# instant of table exams
Exams_instants= Base.classes.exams
# instant of table plan
Plans_instants= Base.classes.plans
#instant of table user
Users_instants = Base.classes.users
#get data

def get_permis(role_id,per_id):
    with engine.begin() as conn:

        res= conn.execute(f'SELECT * FROM add_role WHERE per_id ={per_id} AND role_id = {role_id}').first()
        return res

def get_per_id(permis):
    with engine.begin() as conn:
        res = list(conn.execute(f"SELECT per_id FROM permistions WHERE per_name = '{permis}' ").fetchone())[0]
        if not res:
            return None
        return res

def get_all_data(obj):
    rows= session.query(obj)
    return rows

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
errors={
    "404": [{
        "detail": "ID Unknown",
        "status": 404,
        "title": "Not Found",
        "type": "about:blank"
    },404],
    "400": [{
        "detail": "The server could not understand the request due to invalid syntax",
        "status": 400,
        "title": "Bad Request",
        "type": "about:blank"
    },400],
    "401": [{
        "detail": "the client must authenticate itself to get the requested response",
        "status": 401,
        "title": "Unauthorized",
        "type": "about:blank"
    },401],
    "405": [{
        "detail": "The method request  has been disabled and cannot be used",
        "status": 405,
        "title": "Method not allow",
        "type": "about:blank"
    },405],
    "403": [{
        "detail": "The client does not have access rights to the content",
        "status": 403,
        "title": "Forbidden",
        "type": "about:blank"
    },403]

}