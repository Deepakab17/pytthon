# class Student:
#     pass
# print(id(Student))
# obj=Student
# print(id(obj))
# obj1=Student
# print(id(obj1))
# the memory address is same because it is not assign to other objects... the address belongs to the class

# class Student:
#     '''deepak'''
#     school='SHSS'
#     def showdetails():
#         print("h")
# # print(dir(Student))
# print(Student.__doc__)
# s=Student
# print(s)
# print(print("hello"))
# class Student:
#     pass
# print(id(Student))
# obj=Student()
# print(id(obj))
# obj1=Student()
# print(id(obj1))
# class student:
#     def __init__(self):
#         print("constructor called")
# obj=student
# obj=student()
# class student:
#     def __init__(self):
#         print("constructor called")
#         print(id(self))
# obj=student
# obj=student()
# print(id(obj))
# class Student:
#     def __init__(self,name,quali):
#        self.n=name
#        self.q=quali
# obj=Student("Deepak","Cricketer")
# obj1=Student("Deepak","Cricketer")
# print(id(obj.n))
# print(id(obj1.n))
# class Student:
#     def __init__(self,name,quali):
#        self.n=name
#        self.q=quali
#     #    print(self.n,self.q)
#     def add(self,contact):
#         self.c=contact
#         # print(self.n,self.q,self.c,self.city)
# obj=Student("Deepak","Cricketer")

# obj.city="kolkata"
# x=eval(input("enter contact details\n"))
# obj.add(x)
# print(obj.n,obj.q,obj.c,obj.city)
# class Student:
#     scholl="ABCD"
#     def __init__(self,name,quali):
#        self.n=name
#        self.q=quali
#        Student.grade='10'
#     #    print(self.n,self.q)
#     def add(self):
#         Student.principle="GGGG"
#         # print(self.n,self.q,self.c,self.city)
# Student.school_city='Bhopal'
# obj=Student("Deepak","Cricketer")

# obj.city="kolkata"
# x=eval(input("enter contact details\n"))
# obj.add(x)
# print(obj.n,obj.q,obj.c,obj.city)
# class Student:
#     def __init__(self):
#         x=10
#         print(x)
#     def new(self):
#         y=10
#         print(y)
#         # print(x)

# obj=Student
# obj.new(20)
# class Book:
#     Price=100
#     def __init__(self,title,total_pages):
#         self.t=title
#         self.tp=total_pages
   
#     def update_price(cls,P):
#         cls.Price=P
#         print(id(cls))
# obj=Book('python',200)
# print(obj.t,obj.tp,Book.Price)
# x=float(input("enter updated price"))
# obj.update_price(x)
# obj1=Book('JAVA',200.98)
# print(obj1.t,obj1.tp,Book.Price)
# print(id(Book))

# class Web:
#     def __init__(self,name):
#         self.n=name
#     def greet():
#         print("welcome")
# obj=Web("eccomerce")
# obj.greet()
# # obj=Web
# # obj.greet()
# class Web:
#     def __init__(self,name):
#         self.n=name
#     @staticmethod
#     def greet():
#         print("welcome")
# obj=Web("eccomerce")
# obj.greet()
# obj=Web
# obj.greet()
# class Student:
#     x=10
#     y=20
#     def new(self):
#         print("new")
# obj=Student.new("deep")

# print(Student.x)
# class Parent:
#     watch="RICHARD MILLE"
#     def home(self):
#         print("THIS IS PARENT PROPERTY")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.watch)
# obj.home()
# class Parent:
#     watch="RICHARD MILLE"
#     def home(self):
#         print("THIS IS PARENT PROPERTY")
# class Child(Parent):
#     def home(self):
#         print("this is child home")
#         super().home()
# obj=Child()
# print(obj.watch)
# obj.home()
# class Student:
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#     def new(self,grade):
#         self.g=grade
    
# class Watch:
#     def __init__(self,brand):
#         self.b=brand

    
# obj=Student('raj',101)
# obj=Watch('Richard Mille')
# print(obj)

        

    
    











