# l=[10,20,30,'python']
# l1=[1,2,3,4]
# #l.extend(l1)
# #l.extend([98847,'sharvan'])
# #print(l)
# #print(l.pop())
# l2=l.copy
# #print(id(l1),id(l2))
# l1.sort(reverse=True)
# print(l1)

grade=input('enter your grades here (from A to D) :\n')
grade =(grade,)
if grade in('A', 'B', 'C', 'D'):
    print(grade.count('A'))
else :
    print("invalid Grade : please Try again \n")                               
