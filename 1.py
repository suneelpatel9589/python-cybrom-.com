# # Print numbers from 1 to 10

# i=1
# while(i<=10):
#     print(i)
#     i+=1


# # Print multiplication table of a number
# i=1
# n= int(input('enter a number'))
# while(i<=10):
#     print(f"{n} x {i} = {n*i}")
#     i+=1

# # Calculate the sum of first n natural numbers
# i=1
# n= int(input('enter a number'))
# sum =0
# while(i<=n):
#     sum=sum+i
#     i+=1
# print(sum)

# # Calculate the factorial of a number
# i=1
# n= int(input('enter a number'))
# sum =1
# while(i<=n):
#     sum=sum*i
#     i+=1
# print(sum ,'is the factorial of', n)


# #  Check whether a number is prime or not 
# i=1
# n= int(input('enter a number'))
# sum =0
# while(i<=n):
#     if(n%i==0):
#         sum= sum+1
#     i+=1
# if(sum==2):
#     print(n,'is a prime number')
# else:
#     print(n,'is not a prime number')


# # Reverse a number
# i=1
# n= int(input('enter a number'))
# ans =0
# while(n<0):
#     print("please enter a positive number")
# while(n>0):
#     r= n%10
#     ans =ans*10+r
#     n =n//10
# print(ans,"reverse number")

# # Check whether a number is a palindrome or not
# i=1
# n= int(input('enter a number'))
# ans =0
# m=n
# while(n<0):
#     print("please enter a positive number")
# while(n>0):
#     r= n%10
#     ans =ans*10+r
#     n =n//10
# if(m==ans):
#     print(m,"is a palindrome number")
# else:
#     print(m,"is not a palindrome number")

# # check whether a number is an Armstrong number or not
# i=1
# n= int(input('enter a number'))
# ans =0
# p =len(str(n))
# m=n
# while(n>0):
#     r= n%10
#     ans= ans+r**p
#     n= n//10
# if(ans==m):
#      print(m,"is an armstrong number")
# else:
#     print(m,"is not an armstrong number")


# # Print Fibonacci series up to n terms
# i=1
# n= int(input('enter a number'))
# a=-1
# b=1
# while(i<=n):
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     i+=1

# # Print the pattern
# i =1
# x= 65
# while(i<=5):
#     j=1
#     while(j<=i):
#         print(chr(x),end="")
#         x+=1
#         j+=1
#     print()


# write a program to make a crud operation on list


