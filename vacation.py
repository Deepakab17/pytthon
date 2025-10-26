# n=int(input("enter numb of rows :\n"))
# for i in range(1, n+1):
#       print(' *'*i+''*(n-i))
# n =int(input("Enter number of rows:\n"))
# for i in range(0,n): 
#     print(' '*i +' *'* (n-i))
# n=int(input("enter no of rows\n"))
# for i in range(1,n+1):
#     print(' '*(n-i)+' *'*i)
# x=2
# print(x>>2)
# import keyword

# print(keyword.kwlist)
# print("Total keywords:", len(keyword.kwlist))
# r=1
# print(dir(r))
# h=eval(input("enter any value"))
# print(h,type(h))
# while(True):
#     print("1.Add 2. Substract 3. Multiply 4.Divide 5.Exit")
#     number=int(input("enter any choice\n"))
#     if number in (1,2,3,4,5):
#         if number in (1,2,3,4):
#             if number==1:
#                 sum,l=0,[]
#                 n=int(input("How many number you want to add\n"))
#                 for i in range(1,n+1):
#                     value=int(input(f'Please enter {i} number\n'))
#                     l.append(value)
#                     sum=sum+value
#                 print(f'Sum of {l} is = {sum}')   
#             elif number==2:
#                 sub,l=0,[] 
#                 n=int(input("How many numbers you want to substract\n"))
#                 for i in range(1,n+1):
#                     value=int(input(f'Please enter {i} number\n'))
#                     if i==1:
#                        sub=value
#                        l.append(value)
#                     else:
#                         l.append(value)
#                         sub=sub-value
#                 print(f'The substraction of given {l} is = {sub}')  
#             elif number==3:
#                 mul,l=1,[]
#                 n= int(input("Enter how many numbers you want to multiply\n"))
#                 for i in range(1,n+1):
#                     value=int(input(f'Please enter {i} number\n'))
#                     l.append(value)
#                     mul=mul*value
#                 print(f'The total of given {l} is = {mul}')
#             elif number==4:
#                 div,l=0,[] 
#                 n=int(input("How many numbers you want to divide\n"))
#                 for i in range(1,n+1):
#                     value=int(input(f'Please enter {i} number\n'))
#                     if i==1:
#                        div=value
#                        l.append(value)
#                     else:
#                         l.append(value)
#                         div=div/value
#                 print(f'The division of given {l} is = {div}')            
#         else:
#             break
#     else:
#         print("Chose a valid number")
# number=int(input("Enter a number\n"))
# count=0
# sum=0
# new=number
# original=number
# while number>0:
#     count=count+1
#     number=number//10
# while new>0:
#     digit=new%10
#     sum=sum+digit**count
#     new=new//10
# if sum==original:
#     print("armstrong")
# else:
#     print("not armstrong")
# n=int(input("enter a number:\n"))
# rev=0
# new=n
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==new:
#     print("palindrome")
# else:
#     print("not palindrome")
# n=int(input("enter a number to find factors:\n"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# print(f"the Factors of {n} are {i} ")  
# n=int(input("enter a number to find perfect number:\n"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("this is a perfcect number")  
# else:
#     print("not perfect")  
# n=int(input("enter a number to find prime number\n"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("Prime number")
# else:
#     print("not prime")
# n=int(input("Enter any number\n"))
# count=sum=0
# new=original=n
# while n>0:
#     count=count+1
#     n=n//10
# while new>0:
#     digit=new%10
#     sum=sum+digit**count
#     new=new//10
# if sum==original:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong")
# n=int(input("enter number of rows\n"))
# for i in range(1,n+1):
#     print('*'*i+' '*(n-i))
# n=int(input("enter number of rows to print\n"))
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
# n=int(input("enter number of rows to print\n"))
# for i in range(1,n+1):
#     print(' '*(n-i)+' *'*i)
# n= int(input("enter number of rows\n"))
# for i in range(0,n):
#     print(' '*i+'*'*(n-i))
# n= int(input("enter number of rows\n"))
# for i in range(0,n):
#     print('*'*(n-i)+' '*i)
n=int(input("enter  number of rows\n"))
for i in range(1,n+1):
    print(' '*(n-i)+' *'*i)
for i in range(4,0,-1):
    print(' '*(n-i)+' *'*i)




