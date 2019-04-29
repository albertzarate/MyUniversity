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