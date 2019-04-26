import mysql.connector

sql=mysql.connector.connect(user='myuniversity', password='myuniversity', host='myuniversity.cwscsavqzqxt.us-east-2.rds.amazonaws.com')

print(sql)

sql.close()

# Go here to learn how to use the MySQL wrapper for Python https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

