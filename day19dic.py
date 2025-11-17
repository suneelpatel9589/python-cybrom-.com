
# dicnary
# dicnary is a collection of key and value pair
# dicnary is mutable type
# dicnary is unordered
# dicnary is indexed
# dicnary is mutable

# Method	-   क्या करता है
# keys()	 -  सभी keys देता है
# values()   -  सभी values देता है
# get()	key  -  की value देता है (error नहीं देता)
# pop()	     -  दी हुई key हटाता है
# update()	 -  value अपडेट या नई key जोड़ता है
# popitem()	 -  आखिरी आइटम हटाता है
# fromkeys()  -  नई dictionary बनाता है


# d= {
#     'key':100,
#     'key1':200,
#     'key2':300,
#     'key3':400,
#     'key3':500

# }

# print(d)

# print(d['key1'])
# for i in d.values():
#     print(i)

# x=d.keys()
# print(x)
# x=d.values() #values method
# print(x)
# x=d.get('key2') #get method element access
# print(x)
# x=d.pop('key3') #pop method element remove
# print(x)
# print(d)
# d.update({'key3':'bhopal'}) #update method
# print(d)
# d.popitem() #popitem method element remove last item
# print(d)
# d.fromkeys(['a','b','c'],100) #fromkeys method create dicnary
# print(d)

# pattern program in python 

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('#',end=' ')
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=' ')
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=' ')
#         j+=1
#     print()
#     i+=1


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(chr(64 + i), end=' ')
        j += 1
    print()
    i += 1


