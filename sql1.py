import connection as con
print("press 1 for insert\n press 2 for show\n press 3 for update\n press 4 for delete")
ch=int(input("Enter your choice:"))
ob=con.soon()
if(ch==1):
    name=input("Enter the name:")
    rollno=int(input("Enter the roll no:"))
    email=input("Enter the email:")
    mobile=int(input("Enter the mobile no:"))
    ob.insertdata(name,rollno,email,mobile)

elif(ch==2):
    ob.Show()
elif(ch==3):
    ob.Update()
elif(ch==4):
    ob.delete()
