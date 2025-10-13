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
number=int(input("give a number\n"))
i=1
while i<=number:
    print(''*(number-i)+'*'*i)
    i=i+1
i=i-2
while i>=1:
    print(''*(number-i)+'*'*i)
    i=i-1
