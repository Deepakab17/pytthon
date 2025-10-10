number=int(input("enter number of rows to make triangle\n"))
i=1
while i<=number:
    print(' '*(number-i)+'*'*i)
    i=i+1
i=i-2
while i>0: 
    print(' '*(number-i)+'*'*i)   
    i=i-1