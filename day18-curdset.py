s=set()
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
        print("create")
        ndata=int(input("Enter the no of data:"))
        for i in range(ndata):
            print(f"please enter {i+1} data")
            data=input("Enter the data:")
            s.add(data)
    elif(ch==2):
        print("read")
        print(s)
    elif(ch==3):
        ndata=input("Enter the data to updata:")
        if(ndata in s):
            print("Data match")
            s.remove(ndata)
            udata=input("Enter the updated data:")
            s.add(udata)
        else:
            print("Not match")

    elif(ch==4):
        ddata=input("Enter the data for delete:")
        if(ddata in s):
            s.remove(ddata)
    elif(ch==5):
        print("exit")
        break
    else:
        print("wrong choice")