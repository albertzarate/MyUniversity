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

def getEmail(sid):
	query = select([student_info.c.email]).where(student_info.c.student_id == sid)
	userEmail = connectDB(query)
	return userEmail[0]

def getInfo(email):
	query = select([student_info]).where(student_info.c.email == email)
	userInfo = connectDB(query)
	return userInfo[0]

def getEnrollment(sid):
	query = select([enrollment_info.c.course_id]).where(enrollment_info.c.student_id == sid)
	userEnrollment = connectDB(query)
	enrollment = []
	for course in userEnrollment:
		course = dict(course.items())
		query = select([course_info]).where(course_info.c.course_id == course['course_id'])
		result = connectDB(query)
		if result:
			enrollment.append(dict(result[0].items()))
	return enrollment

def verifyLogin(email):
	query = select([func.count(student_info.c.email)]).where(student_info.c.email == email)
	isVerified = connectDB(query)
	isVerified = dict(isVerified[0].items())
	if isVerified['count_1']:
		return True
	else:
		return False
