import json
json_data = [{'name':'Sara', 'id':1, 'salary':30000}, {'name':'John', 'id':2, 'salary':40000}
             , {'name':'Mike', 'id':3, 'salary':35000}, {'name':'Andy', 'id':4, 'salary':50000}]
res = json.dumps(json_data)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE JSONDATA ")

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="jsondata"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE employee (name VARCHAR(255),id INT, salary DOUBLE")

dbse = mydb.cursor()
sql = "INSERT INTO employee (name, id, salary) VALUES (%s)"
for i in res:
    x = res[i]
value = list(x)
dbse.execute(sql, value)
