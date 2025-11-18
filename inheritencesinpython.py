# class GrandParent:
#     def home(self):
#         print("grandparent")
#     def car(self):
#         print("car of GP")
# class Parent(GrandParent):
#     def home(self):
#         print("parent")
#         super().home()
#     def watch(self):
#         print("RICHARD MILLE")

# class Child(Parent):
#     def home(self):
#         print("child")
#         super().home()
# obj=Child()
# obj.watch()
# obj.car()
# class Parent1:
#     def home(self):
#         print("grandparent")
#         Parent2.home(self)
#     def car(self):
#         print("car of GP")
# class Parent2:
#     def home(self):
#         print("parent")
      
#     def watch(self):
#         print("RICHARD MILLE")

# class Child(Parent1,Parent2):

#     def home(self):
#         print("child")
#         super().home()
# obj=Child()
# obj.home()
# obj.car()

