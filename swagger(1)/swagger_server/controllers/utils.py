from sqlalchemy import create_engine



engine = create_engine('mssql+pymssql://sa:Thienphu1@WIN-95DVFJUNMEL:1433/ManagementStudents')
'''
def get_data():
    with engine.begin() as conn:
        rows= conn.execute('SELECT * FROM Teachers')
        data=[]
        for row in rows:
            data.append({
                'FullName': row[1]
            })
        return data'''
with engine.connect() as conn:
    cur = conn.cursor()
    print(cur.execute('SELECT @@version'))
    cur.close()