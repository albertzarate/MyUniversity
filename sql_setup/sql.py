from sqlalchemy import inspect, create_engine, MetaData, Table, select, or_, and_, join
from sqlalchemy.engine import reflection


engine = create_engine('mysql://(username):(password)http://ec2-18-222-192-36.us-east-2.compute.amazonaws.com/(database name)')
inspector = inspect(engine)
meta = MetaData(engine,reflect=True)
student_info = meta.tables['student_info']
teacher_info = meta.tables['teacher_info']
Login_info = meta.tables['Login_info']
transaction_details = meta.tables['transaction_details']
building_info = meta.tables['building_info']
room_info = meta.tables['room_info']
course_info = meta.tables['course_info']

def connectDB(query): 
    conn = engine.connect()
    res = conn.execute(query)
    engine.dispose()
    return list(res)
