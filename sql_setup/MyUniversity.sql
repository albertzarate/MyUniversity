CREATE DATABASE MyUniversity;
USE MyUniversity;


create table student_info(
	student_id char(9) NOT NULL UNIQUE,
	first_name varchar (255) NOT NULL,
	last_name varchar (255) NOT NULL,
	middle_name varchar (255) NOT NULL,
	email varchar (255) NOT NULL, 
	address varchar (255) NOT NULL,
	enrolled BOOLEAN NOT NULL,
	major varchar (255) NOT NULL,
	minor varchar (255),
	expected_grad_year INT,
	expected_grad_sem varchar (255),
	balance INT NOT NULL,
	PRIMARY KEY (student_id)
);
create table Login_info(
	student_id char(9) NOT NULL UNIQUE,
	username varchar (255) NOT NULL UNIQUE,
	password varchar (255) NOT NULL,
	FOREIGN KEY (student_id) REFERENCES student_info(student_id)
);

create table transaction_details(
	student_id char(9) NOT NULL,
	transaction_id INT UNSIGNED NOT NULL UNIQUE,
	amount INT NOT NULL,
	deposit BOOLEAN NOT NULL,
	note varchar (255),
	transaction_title varchar (255),
	PRIMARY KEY (transaction_id),
	FOREIGN KEY (student_id) REFERENCES student_info(student_id)
);

create table building_info(
	building char(4) NOT NULL UNIQUE,
	building_name varchar(255) NOT NULL,
	PRIMARY KEY (building)
);

create table room_info(
	room_id char(6) NOT NULL UNIQUE,
	building char(4) NOT NULL,
	room_number INT(4) NOT NULL,
	max_occupancy INT(4) NOT NULL,
	PRIMARY KEY (room_id),
	FOREIGN KEY (building) REFERENCES building_info (building)
);

create table teacher_info(
	teacher_id char(9) NOT NULL UNIQUE,
	first_name varchar (255) NOT NULL,
	last_name varchar (255) NOT NULL,
	middle_name varchar (255) NOT NULL,
	phone char(14) NOT NULL,
	building char(4) NOT NULL,
	room_id char(6) NOT NULL,
	currently_employed BOOLEAN,
	PRIMARY KEY (teacher_id),
	FOREIGN KEY (room_id) REFERENCES room_info (room_id),
	FOREIGN KEY (building) REFERENCES room_info (building)
);

create table course_info(
	course_id char(6) NOT NULL UNIQUE,
	name varchar(255) NOT NULL,
	description char(255) NOT NULL,
	room_id char(9) NOT NULL,
	year INT UNSIGNED NOT NULL,
	semester char(6) NOT NULL,
	teacher_id char(9) NOT NULL,
	enrolled_amount INT UNSIGNED NOT NULL,
	PRIMARY KEY (course_id),
	FOREIGN KEY (room_id) REFERENCES room_info (room_id),
	FOREIGN KEY (teacher_id) REFERENCES teacher_info (teacher_id)
);