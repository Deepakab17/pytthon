# number=int(input('enter a number\n'))
# i=1
# while i<=number:
#     if i<number:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+1
# number=int(input('enter a number\n'))
# i=1
# while i<=number:
#     if i<number:
#         print(i,end='+')
#     else:
#         print(i)
#     i=i+1
# number=int(input('enter a number\n'))
# sum=0
# i=1
# while i<=number:
#     sum=sum+i
#     if i<number:
#         print(i,end='+')
#     else:
#         print(i, end='=')
#     i=i+1
# print(sum)
number=int(input('enter a number\n'))
multi=1
i=1
while i<=number:
    multi=multi*i
    if i<number:
        print(i,end='+')
    else:
        print(i, end='=')
    i=i+1
print(multi)

    