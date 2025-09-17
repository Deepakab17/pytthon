number=int(input("enter a number between 1 to 500"))
if   number==17: 
     print("you are correct")
elif number<17  :
     print("you are close: try upper")
elif number>100 and number<500 :  
     print ("you are too far: try lower")
elif number>17 and number <=100 : 
     print("you are mighty close: try lower") 
else :
      print("sorry mate : invalid number;")