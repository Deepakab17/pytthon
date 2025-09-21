#a = [1,2,3,4,5,4,7]
#print(a.index(4, a.index(4)+1))
name=input("enter your name\n")
number=input('enter your mobile number\n')
reversed_sentence=name[::-1]
reversed_number=number[::-1]
if (len(number)==10):
    print("reversed sentence is", reversed_sentence, "reversed number is ", reversed_number)
else :
    print("invalid number: please try again") 