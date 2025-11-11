# tupple--when we want to respresent multiple value in single entity then we use tupple.
# note: tupple is immutable(change is a not possible)

tup = (1,2,3,4,5,6,7,8,9,10)
print(type(tup))
print(tup[3])

tup1=[]
while(True):
    print('''
    press 1 for create data:
    press 2 for read data:
    press 3 for update data:
    press 4 for delete data:
    press 5 for exit:
''')
    ch=int(input("Enter your choice:"))
    if(ch==1):
        mylist=list(tup1)
        print("create")
        ndata=int(input("Enter the no of data:"))
        for i in range(ndata):
            print(f"please enter {i+1} data")
            data=input("Enter the data:")
            mylist.append(data)
        tup1=tuple(mylist)
    elif(ch==2):
        print("read")
        print(mylist)
    elif(ch==3):
        mylist=list(tup1)
        data=input("Enter the data for update:")
        for i in mylist:
            try:
                x=mylist.index(data)
                udata=input("Enter the updated data:")
                mylist[x]=udata
                break
            except:
                print("Sorry data not found")
        tup1=tuple(mylist)
                
    elif(ch==4):
        mylist=list(tup1)
        ddata=int(input("enter the no. of data to delete:"))
        for i in range(ddata):
            print(f"Insert {i+1} data")
            data=input("Enter the data:")
            try:
                x=mylist.index(data)
                mylist.pop(x)
            except:
                print("data not found")
        tup1=tuple(mylist)
    elif(ch==5):
        print("exit")
        break
    else:
        print("wrong choice")




