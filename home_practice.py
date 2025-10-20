# fm=input('your favourite movie\n').upper()
# fp=input('your favourite player\n').upper()
# fp1=input('who is your favourite person\n').upper()
# favourite=[]
# favourite.append(fm)
# favourite.append(fp)
# favourite.append(fp)
# print(f'your favourite movie is {fm}, player is {fp} and person is {fp1} :')
# orders=[]
# order1=input('what is your order no 1\n').upper()
# order2=input('what is your order no 2\n').upper()
# order3=input('what is your order no 3\n').upper()
# orders.append(order1)
# orders.append(order2)
# orders.append(order3)
# print(f"your order 1 is {order1}, order 2 is {order2}, order 3 is {order3} coming right up, 'THANK YOU DOR YOUR PATIENCE' :")
# number=input("enter a value to check palindrome\n")
# number1=list(number)
# new_number=number1.copy()
# new_number.reverse()
# if(new_number==number1):
#     print("it is a palindrome")
# else :
#     print('not a palindrome')    
# number=int(input("give a number\n"))
# i=1
# while i<=number:
#     print(''*(number-i)+'*'*i)
#     i=i+1
# i=i-2
# while i>=1:
#     print(''*(number-i)+'*'*i)
#     i=i-1
while(True):
    print("1.Addition 2. Substraction 3.Multiplication 4.Division 5.Exit")
    n=int(input('enter any of the given options\n'))
    if n in(1,2,3,4,5):
        if n in (1,2,3,4):
            if n==1:
                sum,l=0,[]
                n=int(input('enter how many numbers you want to add.\n'))
                for i in range(1,n+1):
                    value=int(input(f'enter number {i} value\n'))
                    l.append(value)
                    sum=sum+value 
                print(f'The sum of given {l} is {sum}')
            elif n==2:
                sub,l=0,[]
                n=int(input("enter how many numbers you want to substract\n"))  
                for i in range(1,n+1): 
                    value=int(input("enter number {i} value\n"))  
                    if i==1:
                       sub=value
                       l.append(value)
                    else:
                        l.append(value)
                        sub=sub-value
                print(f'The substraction of your {l} is {sub}')    
            elif n==3:
                multi,l=1,[]
                n=int(input('enter how many numbers you want to multiply\n'))
                for i in range(1,n+1):
                    value=int(input(f'Enter number {i} value\n'))
                    l.append(value)
                    multi=multi*value
                print(f'The multiplication of {l} is {multi}')    

            elif n==4:
                division,l=1,[] 
                n=int(input('Enter how many numbers you want to divide\n'))
                for i in range(1,n+1):
                    value=int(input(f'enter number {i} value\n'))
                    if i==1:
                        division=value
                        l.append(value)
                    else:
                        l.append(value)
                        division=division//value
                print(f'The division of {l} is {division}')           
        else:
            break
    else:
        print('Please enter valid number')

