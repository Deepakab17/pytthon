# s=input('enter any string')
# for i in s:
#     print(i)
# t=eval(input("enter any tuple"))
# for i in t:
#     print(i)
# d=eval(input('enter key value pairs\n'))
# for i in d.values():
#     print(i)
# n=int(input('enter any number\n'))
# for i in range(0,n):
#     print(''*i+'*'*(n-i))
# n=int(input('enter no of rows: \n'))
# for i in range(1,n+1):
#     print('*'*i)
# n=int(input("enter a number :\n"))
# for i in range(0,n):
#     print(' '*i+'*'*(n-i))
# n=int(input("enter a number :\n"))
# for i in range(0,n):
# #     print(' '*i+'* '*(n-i))
# n=int(input("enter a number :\n"))
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
# n=int(input('enter any rows :\n'))
# for i in range(0,n):
#     print()
# n=int(input('enter any number'))
# i=1
# while i<=n:
#     if (i%2!=0):
#         i=i+1
#         continue
#     else:
#         print(i)
#     i=i+1
# n=int(input('enter any number'))
# i=1
# while i<=n:
#     if (i%2 !=0):
#         pass
#     else:
#         print(i)
#     i=i+1 
# n=int(input('enter terms'))
# a=0
# b=1
# c=0
# while c<=n:
#     print(c)
#     a=b
#     b=c
#     c=a+b
# n=int(input('enter a number\n'))
# for i in range(0,n):
#     print(''*i+'*'*(n-i))
# n=int(input('enter any number\n'))
# for i in range(1,n+1):
#     print('*'*i+''*(n-i))/
# n=int(input('enter a number\n'))
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
# n=int(input("enter a number\n"))
# for i in range(0,n):
#     print(' '*i+'*'*(n-i))
n=int(input('enter nuber to print double triangle\n'))
for i in range(1,n+1):
    print('* '*i+' '*(n-i))
for i in range(n,0,-1):
    print('* '*i+' '*(n-1))    



