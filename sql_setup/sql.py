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

def UpdateData(query):
	conn = engine.connect()
	res = conn.execute(query)
	engine.dispose()
	if res.returns_rows:
		return json.dumps([dict(r) for r in res], default=alchemyencoder,encoding='latin-1  ')


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

def getEnrollment(key):
	query = select([enrollment_info.c.course_id]).where(enrollment_info.c.student_id == key)
	userEnrollment = connectDB(query)
	return userEnrollment

def getCourseInfo(key):
	y = []
	for x in key:
		query = select([course_info]).where(course_info.c.course_id == x)
		y.append(connectDB(query))
	return y

def verifyLogin(key):
	query = select([func.count(student_info.c.email)]).where(student_info.c.email == key)
	isVerified = connectDB(query)
	return isVerified[0]

def verifyLogin(key_pass, key_email):
	query = select([func.count(Login_info.c.email)]).where(and_(
                                                Login_info.c.email == key_email,
                                                Login_info.c.password == func.md5(key_pass)
                                                ))
	isValid = connectDB(query)
	return isValid[0]

def UpdatePassword(key, new_password):
	query = Login_info.update().where(Login_info.c.email==key).values(password = new_password)
	UpdateData(query)

def UpdateEmail(key, new_email):
	query = Login_info.update().where(Login_info.c.email==key).values(email = new_email)
	UpdateData(query)

def UpdateAddress(key, new_address):
	query = student_info.update().where(student_info.c.email == key).values (address = new_address)
	UpdateData(query)

def getEnrollemtData(key):
	query = select([enrollment_info.c.course_id]).where(enrollment_info.c.student_id == key)
	userEnrollment = connectDB(query)
	for course_id in userEnrollment:
		query = select([enrollment_info.c.course_id]).where(enrollment_info.c.student_id == key)

def getEnrollment(sid):
	query = select([enrollment_info.c.course_id]).where(enrollment_info.c.student_id == sid)
	userEnrollment = connectDB(query)
	count = 0
	enrollment = []
	teacher = []
	room = []
	for course in userEnrollment:
		course = dict(course.items())
		query = select([course_info]).where(course_info.c.course_id == course['course_id'])
		result = connectDB(query)
		if result:
			enrollment.append(dict(result[0].items()))
	for i in enrollment:
			teacher.append(i['teacher_id'])
			room.append(i['room_id'])
			count += 1
	for i in range(0, count): 
		query = select([teacher_info]).where(teacher_info.c.teacher_id == teacher[i])
		teacherInfo = connectDB(query)
		enrollment[i]['f_name'] = teacherInfo[0][1]
		enrollment[i]['l_name'] = teacherInfo[0][2]
		enrollment[i]['m_name'] = teacherInfo[0][3]
		query = select([room_info]).where(room_info.c.room_id == room[i])
		roomInfo = connectDB(query)
		enrollment[i]['Building'] = roomInfo[0][1]
		enrollment[i]['Room Number'] = roomInfo[0][2]
	return enrollment
	
## def importLogin(key, password):
##    query = Login_info.update().where(Login_info.c.email == key).values(Login_info.c.password = func.md5(password))
##    abc = connectDB(query)
    