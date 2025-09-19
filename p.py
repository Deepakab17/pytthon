name=input("enter your name :")
mobile_number=input("enter your 10 digits mobile number :") 
reversed_name=name[::-1]
card_number="XXXXXX"+mobile_number[-6:-4]+'XX'
if (len (mobile_number)==10): 


    print("Your reversed name is", reversed_name , " and Your card number is :", card_number)
else :
    print("sorry: number incorrect,Try again")
