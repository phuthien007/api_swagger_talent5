from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://postgres:Thienphu1@localhost:5432/ManagementStudents')

Session= sessionmaker(engine)
session= Session()
#get data
def get_all_data(obj):
    with engine.begin() as conn:
        sql= f'''
    SELECT * FROM {obj}
    '''
        rows= conn.execute(sql)
        if rows == None or rows == "":
            return None
        return rows
    
def get_data_by_id(obj, id):
    with engine.begin() as conn:
        sql =f'''
            SELECT * FROM {obj}s
            WHERE {obj}_id = {id}
        '''
        row= conn.execute(sql).fetchone()
        if row == None or row == "":
            return None 
        return row


def add_data(sql):
    with engine.begin() as conn:
        status= conn.execute(sql)
        if status == '':
            return True
        else:
            return False