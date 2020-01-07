import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE members(id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), membershipPlan VARCHAR(20), startDate DATE , age INT)"

cursor.execute(sql)
