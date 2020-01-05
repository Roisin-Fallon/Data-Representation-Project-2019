<<<<<<< HEAD
import mysql.connector       # pip3 install mysql-connector-python
import dbconfig as cfg

class MemberDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )
    
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into members (email, membershipPlan, startDate, age) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
# Note here we return the ID of the last one created 
        self.db.commit()
        return cursor.lastrowid

# getAll this basically gets all and returns back the array 

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from members"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray
    

# findByID we pass in the ID and make a tuple with the ID when executed the %s will become the ID 
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from members where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)  


# Update: cursor updates self members for the tuple (name equals the first entry, age is second and ID is the third) 

    def update(self, values):
        cursor = self.db.cursor()
        sql="update members set email= %s, membershipPlan= %s, startDate= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
 
# delete justs takes in the ID and deletes that

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from members where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("Member is now deleted!")

    def convertToDictionary(self, result):
        colnames=['id','email','membershipPlan','startDate','age']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    

# Makes a new instance of the studentDAO so when I am testing it 
=======
import mysql.connector
import dbconfig as cfg 

# Note by convention classes begin with a capital letter. 
class MemberDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['username'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )
 
# Create: the cursor is to get the database from this class and then do the insert. 
# Note it is the values that is passed into the function!
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into member (email, membershipPlan, startDate, age) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
# Note here we return the ID of the last one created 
        self.db.commit()
        return cursor.lastrowid

# getAll this basically gets all and returns back the array 
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from member"
        cursor.execute(sql)
        result = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.memberDictionary(result))

# findByID we pass in the ID and make a tuple with the ID when executed the %s will become the ID 
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from member where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.memberDictionary(result)


# Update: cursor updates self students for the tuple (name equals the first entry, age is second and ID is the third) 
    def update(self, values):
        cursor = self.db.cursor()
        sql="update member set email= %s, membershipPlan=%s, startDate=%s,  age=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
 
# delete justs takes in the ID and deletes that
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from member where id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.db.commit()
        print("Delete now complete")

    def memberDictionary(self, result):
        colnames=['id','email','membershipPlan','startDate', 'age']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        

# Makes a new instance of the studentDAO so when I am testing it 
>>>>>>> f6390b447151160f9f6daed6f6c5a9e119c1ac31
memberDAO = MemberDAO()