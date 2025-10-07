# i=1
# while i<=10:
#     print("this is number", i)
#     i=i+1
# print('value of i is', i)
# i=5
# while i>=1:
#     print(i)
#     i=i-1

# number=int(input("enter any number to print table\n"))
# i=1
# while i<=10:
#     print(f'{number}*{i} =({number*i}) ')
#     i=i+1
# l=[1,4,8,16,84,100]
# idx=0
# while idx<=(len(l)-1):
#     print(l[idx])
#     idx= idx+1
number=int(input("enter number to find the element \n"))
num=(1,4,8,16,84,100,200,80,44,147,17)
i=0
while i<len(num):
    if (num[i]==number):
        print(f'your number {number} exists at no {i+1} position which is index no {i}')
        break
    i=i+1
else:
        print(f'your given {number} does not exist ')
        


