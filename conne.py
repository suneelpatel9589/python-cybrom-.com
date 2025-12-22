class son:
    def __init__(self):
        import mysql.connector
        self.mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            database="student"
        )
        self.mycursor=self.mydb.cursor()
    def insert(self,roll,name,city):
        self.roll=roll
        self.name=name
        self.city=city
        sql="insert into details (roll,name,city) value(%s,%s,%s)"
        value=[roll,name,city]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print('insert success')
    def show(self):
        print('details')
        sql="select * from details"
        self.mycursor.execute(sql)
        data= self.mycursor.fetchall()
        for i in data:
            print(i)
    def update(self):
        roll=input('enter update roll no')
        name=input("enter update name")
        city=input('enter update city')
        sql="update details set name=%s,city=%s where roll=%s"
        value=[name,city,roll]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print('updated data')
    def delete(self):
        print('details')
        sql="select * from details"
        self.mycursor.execute(sql)
        data= self.mycursor.fetchall()
        for i in data:
            print(i)
        roll= input("enter a roll number")
        sql1="select * from details where rollno=%s"
        value1=[roll]
        self.mycursor.execute(sql1,value1)
        data=self.mycursor.fetchall()
        myrow=self.mycursor.rowcount
        if(myrow>=1):
            sql="delete from details where rollno=%s"
            self.mycursor.execute(sql,value1)
            self.mydb.commit()
            print("Record deleted successfully......")




    