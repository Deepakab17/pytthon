n=int(input('enter any number\n'))
original=number=n
sum=count=0
while n>0:
    count=count+1
    n=n//10
# print(f'total_digits of {original} is {count}')  
while original>0:
    digit=original%10
    sum=sum+digit**count
    original=original//10
if  number==sum:
    print('armstrong')
else:
    print('not armstrong')    

    

