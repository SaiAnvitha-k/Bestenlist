#Create a connection for DB and print the version using a python program
import mysql.connector
mydb = mysql.connector.connect(
  host ="server name",
  user ="user name",
  password ="password"
)
print(mydb)
import sys
cur = mydb.cursor()
cur.execute("Version()")
data = cur.fetchone()
print("Version: ",str(data))


#Create a multiple tables & insert data in table
import mysql.connector

mydb = mysql.connector.connect(
    host="server name",
    user="user name",
    password="password"
)

database = mydb.cursor()
database.execute("create database")
database = mydb.cursor()
database.execute("show database")
for entry in database:
    print(entry)
database = mydb.cursor()

database.execute("CREATE Table office(emp_name VARCHAR(255), emp_id VARCHAR(255))")

database = mydb.cursor()

database.execute("CREATE Table student(stu_name VARCHAR(255), stu_id VARCHAR(255))")

database = mydb.cursor()

database.execute("CREATE Table costumer(costumer_name VARCHAR(255), costumer_id VARCHAR(255))")

database = mydb.cursor()

database.execute("Show Tables")

for value in database:
    print(value)
    
#Create a employee table and read all the employee name in the table using for loop
import mysql.connector

mydb = mysql.connector.connect(
    host="server name",
    user="user name",
    password="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employee1(emp_name VARCHAR(255), emp_id int)")
mydb = mysql.connector.connect(
    host="server name",
    user="user name",
    password="password"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Employee1(name,id)VALUES(%s,%s)"
val = [('John',1),('Hannah',2),('Betty',3),('Jo',4)]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM Employee1")
myresult = mycursor.fetchall()
for x in myresult:
   print(x)
