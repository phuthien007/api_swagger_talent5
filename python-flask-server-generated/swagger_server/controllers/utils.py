import urllib
from sqlalchemy import create_engine



engine = create_engine('mssql+pyodbc://WIN-95DVFJUNMEL/ManagementStudents?driver=SQL+Server+Native+Client+11.0')

def get_data():
    with engine.begin() as conn:
        rows=conn.execute('SELECT * FROM Teachers')
        data=[]
        for row in rows:
            data.append({
               "FullName": row[1] 
            })
        return data