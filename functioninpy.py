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

save_user(id='1',name= 'Deepak',age='23')