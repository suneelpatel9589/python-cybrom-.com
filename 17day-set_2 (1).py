s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8,9}
print(type(s1))
x=s1.intersection(s2)
print(x)
x=s1.union(s2)
print(x)
x=s1.difference(s2)
print(x)
x=s2.difference(s1)
print(x)

ls=[i for i in range(1,101)]
print(ls)

ls=[i*2 for i in range(1,101)]
print(ls)

tp=(i*2 for i in range(1,101))
print(tp)

s3={i for i in range(1,11)}
print(s3)