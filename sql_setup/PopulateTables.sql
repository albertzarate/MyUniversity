#dont check if foriegn key is there
SET FOREIGN_KEY_CHECKS = 0;

#populates student_info table
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("024147310", "David", "Bond", "James", "whoisthis@gmail.com", "1 Washington Sq, san jose, ca 95112", TRUE, "Art", "Graphic Design", 2021, "Fall", 0);
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("024147220", "Ijaaz", "Ramirez", "Taco", "ilovetacobell@yahoo.com", "78340 Via Clemente, La Quinta, CA 92270", False, "Art", "Graphic Design", 2018, "Spring", 0);
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("024147209", "Mark", "Mathews", "Navina", "mark@gmail.com", "27 N 6th street, san jose, ca 95112", TRUE, "CS", "N/A", 2020, "Fall", 0);
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("010241245", "Donald", "Lifestyle", "Change", "donald.Lifestyle@gmail.com", "27 N 6th street, san jose, ca 95112", TRUE, "CmpE", "math", 2019, "Fall", 0);
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("102341789", "Meghan", "Markle", "James", "suits@gmail.com", "1 Cambridge Lane, Westminister, UK 95012-31", TRUE, "Pre-Law", "HR Management", 2023, "Spring", 0);

#populates login info table
INSERT INTO Login_info (student_id, username, password) values ("024147310" , "Prince Donald", MD5("hashmypassword"));
INSERT INTO Login_info (student_id, username, password) values ("024147220" , "CrazyGOAT", MD5("Wildin@2019"));
INSERT INTO Login_info (student_id, username, password) values ("024147209" , "Mathews1999", MD5("NavinaIsMySister"));
INSERT INTO Login_info (student_id, username, password) values ("010241245" , "Goat", MD5("MI6@2019"));
INSERT INTO Login_info (student_id, username, password) values ("102341789" , "Princess", MD5("tacobell"));

#populates transaction table
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147310", 101224, "-1000", FALSE, "Test value", "Spring Tuition");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147310", 101229, "-5.45", FALSE, "Overdue Books", "Library");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147220", 101225, "-3490.60", FALSE, "Full Time Student", "Fall Tuition");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147220", 101310, "3490.60", TRUE, "Chase Bank ID 010418012, Routing 2413123", "Student Deposit");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147209", 111111, "-10.90", FALSE, "Ticket on 9/5/18", "SJSU Parking Ticket: West Garage");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("024147209", 101231, "-3490.60", FALSE, "Full Time Student", "Fall Tuition");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("010241245", 101232, "-3490.60", FALSE, "Full Time Student", "Fall Tuition");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("102341789", 101233, "-3490.60", FALSE, "Full Time Student", "Fall Tuition");
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("102341789", 101234, "5000", TRUE, "Chase Bank ID 010418012, Routing 2413123", "Fall Tuition");

#populates building info
INSERT INTO building_info (building, building_name) values ("HGH", "Hugh Ghillis Hall");
INSERT INTO building_info (building, building_name) values ("ENGR", "Charles W. Davidson Engineering");
INSERT INTO building_info (building, building_name) values ("CBC", "Classroom Building C");


#create functions to setup rooms for each building
delimiter //
CREATE PROCEDURE ENGRSetup()
BEGIN
    DECLARE i INT DEFAULT 100;
    DECLARE j INT DEFAULT 100101;
    WHILE i <= 390 DO
        INSERT INTO room_info (room_id, building, room_number, max_occupancy) VALUES (j, "ENGR" , i, 30);
        SET i = i + 2;
        SET j = j + 1;
    END WHILE;
END;
//
delimiter ;

delimiter //
CREATE PROCEDURE HGHSetup()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE j INT DEFAULT 200101;
    WHILE i <= 250 DO
        INSERT INTO room_info (room_id, building, room_number, max_occupancy) VALUES (j, "HGH" , i, 30);
        SET i = i + 2;
        SET j = j + 1;
    END WHILE;
END;
//
delimiter ;

delimiter //
CREATE PROCEDURE CBCSetup()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE j INT DEFAULT 300101;
    WHILE i <= 100 DO
        INSERT INTO room_info (room_id, building, room_number, max_occupancy) VALUES (j, "CBC" , i, 30);
        SET i = i + 2;
        SET j = j + 1;
    END WHILE;
END;
//
delimiter ;

#populates room_info table
CALL CBCSetup();
CALL HGHSetup();
Call ENGRSetup();

#populates teacher_info table
INSERT INTO teacher_info (teacher_id, first_name, last_name, middle_name, phone, building, room_id, currently_employed) values ("070418411", "Josh", "Tallboy", "Mark", "(760)-741-7321", "HGH", 130, TRUE);
INSERT INTO teacher_info (teacher_id, first_name, last_name, middle_name, phone, building, room_id, currently_employed) values ("070418412", "Andrew", "Bond", "James", "(408)-412-7321", "ENGR", 337, TRUE);
INSERT INTO teacher_info (teacher_id, first_name, last_name, middle_name, phone, building, room_id, currently_employed) values ("027914122", "Ozemek", "Haluk", "CYL", "(298)-741-4041", "CBC", 010, FALSE);
INSERT INTO teacher_info (teacher_id, first_name, last_name, middle_name, phone, building, room_id, currently_employed) values ("070418418", "Josh", "Tallboy", "Mark", "(760)-741-7321", "HGH", 270, TRUE);
INSERT INTO teacher_info (teacher_id, first_name, last_name, middle_name, phone, building, room_id, currently_employed) values ("070418422", "Akash", "Vachhani", "Kishor", "(510)-291-2421", "ENGR", 294, TRUE);


#update balance on student info table based off transaction history
UPDATE student_info s
INNER JOIN
(
   SELECT student_id, SUM(amount) 'sumu'
   FROM transaction_details 
   GROUP BY student_id
) i ON s.student_id = i.student_id
SET s.balance = i.sumu
WHERE s.student_id = 024147310;

UPDATE student_info s
INNER JOIN
(
   SELECT student_id, SUM(amount) 'sumu'
   FROM transaction_details 
   GROUP BY student_id
) i ON s.student_id = i.student_id
SET s.balance = i.sumu
WHERE s.student_id = 024147220;

UPDATE student_info s
INNER JOIN
(
   SELECT student_id, SUM(amount) 'sumu'
   FROM transaction_details 
   GROUP BY student_id
) i ON s.student_id = i.student_id
SET s.balance = i.sumu
WHERE s.student_id = 024147209;

UPDATE student_info s
INNER JOIN
(
   SELECT student_id, SUM(amount) 'sumu'
   FROM transaction_details 
   GROUP BY student_id
) i ON s.student_id = i.student_id
SET s.balance = i.sumu
WHERE s.student_id = 010241245;

UPDATE student_info s
INNER JOIN
(
   SELECT student_id, SUM(amount) 'sumu'
   FROM transaction_details 
   GROUP BY student_id
) i ON s.student_id = i.student_id
SET s.balance = i.sumu
WHERE s.student_id = 102341789;


############################################################################################
#Disaply Information after Above

SELECT *
FROM student_info;

SELECT *
FROM Login_info;

SELECT *
FROM transaction_details;



