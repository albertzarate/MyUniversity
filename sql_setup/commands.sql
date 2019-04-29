
#insert information into Student_Info Table
INSERT INTO student_info (student_id, first_name, last_name, middle_name, email, address, enrolled, major, minor, expected_grad_year, expected_grad_sem, balance) VALUES ("010241245", "Donald", "Lifestyle", "Change", "donald.Lifestyle@gmail.com", "27 N 6th street, san jose, ca 95112", TRUE, "CmpE", "math", 2019, "Fall", 0);

#insert information into login_info table
INSERT INTO Login_info (student_id, username, password) values ("010241245" , "Prince Donald", MD5("hashmypassword"));

#insert information into transcation_details table
INSERT INTO transaction_details (student_id, transaction_id, amount, deposit, note, transaction_title) values ("010241245", 005, "-1000", FALSE, "Test value", "Tuition");

#update the balance of students after a deposit or bill is posted in the transaction table
UPDATE student_info (balance) SELECT SUM(amount) FROM transaction_details WHERE student_id = 010241245;
