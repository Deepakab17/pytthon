n=int(input("enter a number\n"))
count=0
sum=0
original=n
new=n
while n>0:
    count=count+1
    n=n//10
while new>0:
    digit=new%10
    sum=sum+digit**count
    new=new//10
if original==sum:
    print('armstrong')
else:
    print('not armstrong')        

   


    

