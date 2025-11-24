# def rect_area(length,width):
#     area=length*width
#     print(area)
# rect_area(14,10)
# unit= "feet Square"
# area=500
# def rect_area(length,width):
#     area=length*width
#     return area
# m_area=rect_area(14,10)
# print(m_area,unit)
# print(area)
# def greet(name):
#     return "Hello "+ name +"!"
# print(greet("Chutki"))
# print(greet("Deepak"))
# def add(a,b):
#     return a+b
# result=add(40,80)
# print(add(result,80))
# def compute(a,b):
#     result=a*b
#     if result > 10:
#         return result -3
#     else:
#         return result +5
# print(compute(5,4))
# print(compute(3,2))
# counter=70
# def increment(value):
#     counter+=value
#     return counter
# print(increment(10))
# print(counter)
# def greet(name):
#     print(f"hi {name}")


# print(greet("deepak"))
#keyword arguments_----------------------------------------
# def increment(number,by):
#     return number+by

# print(increment(5,by=5 ))
#default arguments-----------------------------------------------------------
# def multiply(number, by=2):
#     return number*by

# print(multiply(7))
# args-------------------------------------------------------------------
# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number
#     return total

# print(multiply(4,5,7,8))
# args--------------------------------------
# def save_user(**user):
#     print(user)

# print (save_user(id='1',name= 'Deepak',age='23'))
def save_user(**user):
    print(user["name"])
    print(user)

save_user(id='1',name= 'Deepak',age='23')

# scope______-------------------------------
# message = "b"
# def greet(name):
#     global message
#     message="d"
# greet("deepak")
# print(message)
# def fizz_buzz(input):
#     if input%3==0 and input%5==0:
#        return  "fizzbuzz"
#     if input%3==0:
#        return  "fizz"
#     if input%5==0:
#        return  "buzz"
#     return input
  

# print(fizz_buzz(3))
# def palindrome(number):
#     rev=0
#     original=number
#     while number>0:
#         digit=number%10
#         rev=rev*10+digit
#         number=number//10
#     if rev==original:
#         return "palindrome"
#     else:
#         return "not palindrome"
    
# print(palindrome(121))
# def square(number):
#     return number**2

# result=square(5)
# print(result)

# import math
# def circle(radius):
#     area=math.pi*radius**2
#     circumference=2*math.pi*radius
#     return area, circumference

# a,c=circle(5)
# print("area :",round(a,2), "circumference:", round(c,2))
# def greet(name="Arvind"):
#     return "hello, sailor," + name + " How are you doing today?"

# print(greet())
# def add(*args):
#     print(args)
#     for i in args:
#         print(i*3)
#     return sum(args)

# result=add(1,2,3,4)
# print(result)
 