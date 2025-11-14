
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

