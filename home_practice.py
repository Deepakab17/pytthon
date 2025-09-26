# fm=input('your favourite movie\n')
# fp=input('your favourite player\n')
# fp1=input('who is your favourite person\n')
# favourite=[]
# favourite.append(fm)
# favourite.append(fp)
# favourite.append(fp)

# print('your favourite movie, player and person are :', favourite)
# orders=[]
# order1=input('what is your order no 1\n')
# order2=input('what is your order no 2\n')
# order3=input('what is your order no 3\n')
# orders.append(order1)
# orders.append(order2)
# orders.append(order3)
# print('your orders are as follows :', orders)
number=input("enter a value to check palindrome\n")
number1=list(number)
new_number=number1.copy()
new_number.reverse()
if(new_number==number1):
    print("it is a palindrome")
else :
    print('not a palindrome')    