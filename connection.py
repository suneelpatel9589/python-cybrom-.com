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
ob=Dbconn()
ob.Showrecord()


