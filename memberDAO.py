import mysql.connector       # pip3 install mysql-connector-python
import dbconfig as cfg

class MemberDAO:
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database']
            )

    def __init__(self): 
        self.connectToDB()   

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()
    
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into members (email, membershipPlan, startDate, age) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close
        return lastRowId

# getAll this basically gets all and returns back the array 

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from members"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close
        return returnArray
    

# findByID we pass in the ID and make a tuple with the ID when executed the %s will become the ID 
    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from members where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        member=self.convertToDictionary(result)
        cursor.close()
        return member

# Update: cursor updates self members for the tuple (name equals the first entry, age is second and ID is the third) 

    def update(self, values):
        cursor = self.getCursor()
        sql="update members set email= %s, membershipPlan= %s, startDate= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close() 
        
# delete justs takes in the ID and deletes that

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from members where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def convertToDictionary(self, result):
        colnames=['id','email','membershipPlan','startDate','age']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    
# Makes a new instance of the studentDAO so when I am testing it 
memberDAO = MemberDAO()