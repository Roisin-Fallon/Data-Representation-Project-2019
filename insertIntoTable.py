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
sql="insert into members (email, membershipPlan, startDate, age) values (%s,%s,%s,%s)"

# values = ("maryfallon@yahoo.ie","Daily", "2019-12-11", 21)
# values = ("jameskelly@yahoo.ie","Annually", "2019-11-30", 30)
# values = ("johnbyrne@gmail.com","Daily", "2019-12-20", 18)
values = ("meganryan@gmail.com","Monthly", "2019-12-28", 27)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)