class Student:
    pass
print(id(Student))
obj=Student
print(id(obj))
obj1=Student
print(id(obj1))
# the memory address is same because it is not assign to other objects... the address belongs to the class

class Student:
    '''deepak'''
    school='SHSS'
    def showdetails():
        print("h")
# print(dir(Student))
print(Student.__doc__)
