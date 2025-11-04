
# # sequence in python
# # when we want to grup of individuals entity into an single entity where homogenous as well as heterogenous element is to be allowed and t
# # list are multiple type of data types;--

ls = list()
print(type(ls))
# or
ls1 = []
print(type(ls1))

# # # list are mutable type 
p = [1,2,3,4,5,6,7,8,9]
print(len(p))
print(p[0:7:2])
for i in p:
    print(i)

# # concatenation
s =[12,13,34,55,66,76,765]
s1 =[43,56,13,654,88,87,99]
s2=s+s1
print(s2)

# # method of list:--
# append method
list = []
list.append([1,2,3,4])
print(list[0])


n= int(input('enter a number'))
for i in range(n):
    data =int(input('enter a data'))
    list.append(data)
print(list)    