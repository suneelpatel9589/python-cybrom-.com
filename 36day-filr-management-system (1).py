print("File Management System")
print("To create file press1\nto read the file press2")
ch=int(input("Enter your choice"))
if(ch==1):
    fnm=input("Enter the file name:")
    fdata=input("Enter the file data")
    f=open(fnm,"w")
    f.write(fdata)
    print("created successfully")
    