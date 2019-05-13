from sqlalchemy import *

with open('/var/www/html/flaskapp/config/rds_endpoint.txt', 'r') as file:
    rds_endpoint = file.read().replace('\n', '')

engine = create_engine('mysql+pymysql://myuniversity:myuniversity@{}:3306/MyUniversity'.format(rds_endpoint))
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

def verifyLogin(email):
	query = select([func.count(student_info.c.email)]).where(student_info.c.email == email)
	isVerified = connectDB(query)
	isVerified = dict(isVerified[0].items())
	if isVerified['count_1']:
		return True
	else:
		return False

def UpdateData(query):
	conn = engine.connect()
	res = conn.execute(query)
	engine.dispose()
	if res.returns_rows:
		return json.dumps([dict(r) for r in res], default=alchemyencoder,encoding='latin-1  ')

def UpdateAddress(email, new_address):
	query = student_info.update().where(student_info.c.email == email).values (address = new_address)
	UpdateData(query)

def UpdatePhone(email, new_phone):
	query = student_info.update().where(student_info.c.email == email).values (phone = new_phone)
	UpdateData(query)

def UpdateSecondaryEmail(email, new_sec_email):
	query = student_info.update().where(student_info.c.email == email).values (sec_email = new_sec_email)
	UpdateData(query)

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

def getTransactionDetails(sid):
	query = select([transaction_details]).where(transaction_details.c.student_id == sid)
	transactions = connectDB(query)
	details = []
	for transaction in transactions:
		details.append(dict(transaction.items()))
	return details
