# l=['a','b','c',1,2,3]
# d=dict.fromkeys(l)
# print(d)
# print(type(d))
# d={'x':10,'y':20,'z':30}
# e={'p':10,'q':20,'x':30}
# c=d.update(e)
# print(d)
s={'x':10,'y':20,'name':'aman'}
d=s.setdefault('x',100)
p=s.setdefault('age',37)
print(d)
print(p)