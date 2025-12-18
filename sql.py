import connection as cls
print("press 1 for insert\n press 2 for show \n press 3 for update")
ch=int(input("Enter your choice:"))
ob=cls.Dbconn()
if(ch==1):
    name=input("Enter the name:")
    rollno=int(input("Enter the roll no:"))
    email=input("Enter the email:")
    mobile=int(input("Enter the mobile no:"))
    ob.Recordinsert(name,rollno,email,mobile)

elif(ch==2):
    ob.Showrecord()
elif(ch==3):
    ob.Updaterecord()

