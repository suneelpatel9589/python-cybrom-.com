
# # # sequence in python
# # # when we want to grup of individuals entity into an single entity where homogenous as well as heterogenous element is to be allowed and t
# # # list are multiple type of data types;--

# ls = list()
# print(type(ls))
# # or
# ls1 = []
# print(type(ls1))

# # # # list are mutable type 
# p = [1,2,3,4,5,6,7,8,9]
# print(len(p))
# print(p[0:7:2])
# for i in p:
#     print(i)

# # # concatenation
# s =[12,13,34,55,66,76,765]
# s1 =[43,56,13,654,88,87,99]
# s2=s+s1
# print(s2)

# # # method of list:--
# # append method
# list = []
# list.append([1,2,3,4])
# print(list[0])


# n= int(input('enter a number'))
# list=[]
# for i in range(n):
#     data =int(input('enter a data'))
#     list.append(data)
# print(list)    


# sum of consicutive no.
# ls1 =[-1,2,3,3,4,5,-1,9]
# k=4
# ls1.sort()
# print(ls1)
# s=0
# for i in range(k,len(ls1)):
#     s= s+ls1[i]
# print(s)



# # wAP to sort the given list [3,8,81,17,13,21,5] is an ascendind order without any using inbuilt method?

# p=[3,8,81,17,13,13,21,5]
# for i in range(len(p)):
#     for j in range(i+1,len(p)):
#         if(p[i]>=p[j]):
#             temp =p[i]
#             p[i]=p[j]
#             p[j]=temp
# print(p)
# print("max",p[len(p)-1])
# print('min',p[len(p)-2])
# x =p.count(13)
# print(x)
# p.extend([234])
# print(p)

# p2= p.copy()
# p.clear()
# print(p2)
# print(p)  

# x=max(p2)
# print(x)
# x=min(p2)
# print(x)

# p2.insert(3,2000)
# print(p2)

# x= p2.index(2000)
# print(x)



# ls = [12,33,56,78,56,33,56]
# ls.pop(0)
# print(ls)


# ls =[23,56,45,34,67,34,56]
# ls.remove(56)
# print(ls)

# x = ls.index(56)
# print(x)

# ls.reverse()
# print(ls)

# write a program to make a crud operation on list
# c-> create
# r-> read
# u-> update
# d-> delete

# write a program to make a crud operation on list?
mylist=[]
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
        ndata=int(input('enter a number of data'))
        for i in range(ndata):
            data =int(input('enter a data'))
            mylist.append(data)
           
       
    elif(ch==2):
        print("read")
        print(mylist)
    elif(ch==3):
        print("update")
        data=int(input("Enter the data for update:"))
        for i in mylist:
            #  if(data==i):
            #      print("data match")
            #      x=mylist.index(data)
            #      updatedata=int(input("Enter the updated data:"))
            #      mylist[x]=updatedata
            #      break
            #  else: print("not match")
            try:
                x=mylist.index(data)
                updatedata=int(input("Enter the updated data:"))
                mylist[x]=updatedata
                break
            except:
                print('sorry data not found')

    elif(ch==4):
        print("delete")
    elif(ch==5):
        print("exit")
        break
    else:
        print("wrong choice")


              
