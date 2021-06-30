#create a db with doctor id and patients visited
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE doctors (doct_name VARCHAR(255), doctor_id VARCHAR(255), patients_visited VARCHAR(255)")

mycursor = mydb.cursor()
sql = "INSERT INTO doctors(doct_name,doct_id,patients_visited)VALUES(%s,%s,%s)"
val = [('Kim','1','10'),('Seri','2','12'),('Jinny','3','0'),('Rose','4','6'),('Nancy','5','0'),('Tan','6','3')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount)

#get the doctors who have patients more than 5 patients visited
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM doctors where patients_visited > 5")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#get the doctors with no patients visited
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM doctors where patients_visited = 0")
myresult = mycursor.fetchall()

for x in myresult:
