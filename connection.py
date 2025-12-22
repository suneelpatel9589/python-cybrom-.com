class Dbconn:
    def __init__(self):
        import mysql.connector
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student"
        )
        self.mycursor=self.mydb.cursor()
    def Recordinsert(self,name,rollno,email,mobile):
        self.name=name
        self.rollno=rollno
        self.email=email
        self.mobile=mobile
        sql="insert into details (name,rollno,email,mobile) values(%s,%s,%s,%s)"
        value=[name,rollno,email,mobile]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print("record inserted successfully")
    def Showrecord(self):
        sql="select * from details"
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)
    def Updaterecord(self):
        rollno=input("Enter the roll no for update")
        name=input("Enter the name  update:")
        email=input("Enter the updated email")
        mobile=input("Enter the updated mobile no:")
        sql="update details set name=%s,email=%s,mobile=%s where rollno=%s"
        value=[name,email,mobile,rollno]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
    def Recorddelete(self):
        print("Student records")
        sql="select * from details"
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)
        rollno=input("Enter the roll no for delete:")
        sql1="select * from details where rollno=%s"
        value1=[rollno]
        self.mycursor.execute(sql1,value1)
        mydata=self.mycursor.fetchall()
        myrow=self.mycursor.rowcount
        if(myrow>=1):
            sql="delete from details where rollno=%s"
            self.mycursor.execute(sql,value1)
            self.mydb.commit()
            print("Record deleted successfully......")
        else:
            print("please enter valid roll no...")
        print("Student records")
        sql="select * from details"
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)

    
# ob=Dbconn()
# ob.Showrecord()
   



