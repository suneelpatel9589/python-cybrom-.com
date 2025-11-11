# when we want to represent a group of indivual entity in an single entity where insertion order is not preserved and duplicates are not 
# allowed them we can implemet a set

# NOTE-> set is mutable (Changes allowed)

s={1,2,3,4,5,6,4,5,6,1,2,3,4,5,6,4}
print(s)
s.add(13)
print(s)
s.add((12,13,16))
print(s)
s.pop()
print(s)
s.remove(13)
print(s)
s.discard((12,13,16))
print(s)