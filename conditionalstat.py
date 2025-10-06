# x=eval(input("enter a value\n"))
# if isinstance(x,int):
#  print("user gives integer value")

# integer format ----------------------------

# x= int(input("enter any number\n"))
# if x%2==0:
#     print("given number is even")
# print("thanks for visit")
 
#________________-even and odd________________________
# x=int(input("enter any number\n"))
# if x>0:
#     print("positive")
    
# else:
#     print("nahi hai ji... gali de denge")
year=int(input("enter a year"))
if (year%4==0 and year%100!=0)or year%400==0:
    print("year is leap year")
else ('number is not a leap year')