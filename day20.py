# create an employee table with name , id and salary
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE employee (name VARCHAR(255), id VARCHAR(255), salary VARCHAR(255))")
mycursor = mydb.cursor()
sql = "INSERT INTO employee (name, id, salary) VALUES (%s,%s,%s)"
val = [('John', '1', '200000'), ('Ankitha', '2', '300000'), ('Abbas', '3', '250000'), ('Kang', '4', '100000'),
       ('Emma', '5', '150000')]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount)

# query to get max and min salary from employee table
cursor = mydb.cursor()
cursor.execute("SELECT MAX(Value) AS maximum FROM salary")
result = cursor.fetchall()
for i in result:
    maximum = float(i[0])
    print(maximum)

cursor = mydb.cursor()
cursor.execute("SELECT MIN(Value) AS minimum FROM salary")
result = cursor.fetchall()
for i in result:
    maximum = float(i[0])
    print(maximum)

mydb.close()

# query to get number of employees working with the company
cursor = mydb.cursor()
cursor.execute("SELECT COUNT(*) FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# query to get first 3 characters of first name from employee table
cursor = mydb.cursor()
cursor.execute("SELECT SUBSTRING(name,1,3) FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
