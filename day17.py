# # when we want to represent a group of indivual entity in an single entity where insertion order is not preserved and duplicates are not 
# # allowed them we can implemet a set

# # NOTE-> set is mutable (Changes allowed)

# # s={1,2,3,4,5,6,4,5,6,1,2,3,4,5,6,4}
# # print(s)
# # s.add(13)
# # print(s)
# # s.add((12,13,16))
# # print(s)
# # s.pop()
# # print(s)
# # s.remove(13)
# # print(s)
# # s.discard((12,13,16))
# # print(s)

# s1={1,2,3,4,5,6}
# s2={3,4,5,6,7,8,9}
# print(type(s1))

# # intersection->
# x=s1.intersection(s2)
# print(x)
# # union->
# x=s1.union(s2)
# print(x)
# # difference
# x=s1.difference(s2)
# print(x)
# # symmetric difference
# x=s2.difference(s1)
# print(x)

# ls=[i for i in range(1,101)]
# print(ls)

# ls=[i*2 for i in range(1,101)]
# print(ls)

# tp=(i*2 for i in range(1,101))
# print(tuple(tp))

# # question. create a set of numbers from 1 to 10

# s3={i for i in range(1,11)} 
# print(s3)

#date-12-11-2025
# wap to create a set of numbers from 1 to 10 and add 5 more number
s2= {1,2,3,4,5}
print(s2)
s2.update([6,7,8,9,10])#add
print(s2)

s1={11,12,13,14,15,16}
x= s2|s1 #union
print(x)

s=frozenset({1,2,3,4,5})
s3=frozenset(s)
print(s3)
print(s)
s.add("dff")
print(s)
