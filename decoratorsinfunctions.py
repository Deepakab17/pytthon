# def decorator(x):
#     def inner(p,q,r):
#         p=p+5
#         q=q+10
#         r=r+15
#         z=x(p,q,r)
#         return z
#     return inner
# @ decorator
# def add(a,b,c):
#     return a+b+c
# res=add(2,4,6)
# print(res)
# def decorator(func):
#     def inner(p, q, r):  
#         p = p - 1
#         q = q + 1
#         return func(p, q, r)  
#     return inner

# @decorator
# def even_no(p, q, r):
#     for i in range(p, q, r):
#         if i % 2== 0:
#             print(i)

# even_no(2, 101, 1)

# def outer_func(x):
#     def inner_fun(p,q):
#         p=p+5
#         q=q+50
#         result1=x(p,q)
#         return(result1)
#     return inner_fun
# @outer_func
# def add(a,b):
#     return a+b

# result=add(20,30)
# print(result)
# def natural(n):
#     if n==1:
#         print(1)
#         return 
#     natural(n-1)
#     print(n)
# natural(10)
# def natural(n):
#     if n==0:
#         return None
#     natural(n-1)
#     print(2*n)
# natural(10)
# def natural(n):
#     if n==0:
#         return None
#     natural(n-1)
#     print(2*n-1)
# natural(10)
# def natural(n):
#     if n==0:
#         return 0
#     natural(n-1)
#     sum=natural(n-1)+n
#     return sum
# res=natural(10)
# print(res)

# def pair(**user):
#         return(user)
# name=input("enter your name\n")
# age=int(input("enter your age\n"))
# city=input("enter your city\n")

# result=pair(name=name,age=age,city=city)
# list_of_dictionary=[]
# list_of_dictionary.append(result)
# print(list_of_dictionary)

# def even_no(n):
#     if n==1:
#         print(2)
#         return 
#     even_no(n-1)
#     print(2*n)
# even_no(10)




   




        


