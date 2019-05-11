from sqlalchemy import *


# engine = create_engine('mysql+pymysql://myuniversity:myuniversity@ec2-18-222-192-36.us-east-2.compute.amazonaws.com:3306/MyUniversity')
engine = create_engine('mysql+pymysql://myuniversity:myuniversity@myuniversity.cwscsavqzqxt.us-east-2.rds.amazonaws.com:3306/MyUniversity')
inspector = inspect(engine)
meta = MetaData(engine,reflect=True)
student_info = meta.tables['student_info']
teacher_info = meta.tables['teacher_info']
Login_info = meta.tables['Login_info']
transaction_details = meta.tables['transaction_details']
building_info = meta.tables['building_info']
room_info = meta.tables['room_info']
course_info = meta.tables['course_info']
enrollment_info = meta.tables['enrollment_info']


def connectDB(query): 
	conn = engine.connect()
	res = conn.execute(query)
	engine.dispose()
	return list(res)

def commitDB(table1, data):
	conn = engine.connect()
	conn.execute(table1.insert(), data)

def getEmail(key):
	query = select([student_info.c.email]).where(student_info.c.student_id == key)
	userEmail = connectDB(query)
	return userEmail[0]

def getInfo(key):
	query = select([student_info]).where(student_info.c.email == key)
	userInfo = connectDB(query)
	return userInfo[0]
	

