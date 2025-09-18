x='jython'
y='jython'
print(id(x),id(y))
a=[10,20,'python']
b=[10,20,'python']
print(id(a),id(b))
r=(10,20,'python')
s=(10,20,'python')
print(id(r),id(s))
d={'d':10,'c':20}
c={'d':10,'c':20}
print(id(d),id(c))
m={10,20,'python'}
e={10,20,'python'}
print(id(m),id(e))
n={10,20,'python'}
o={10,20,'python'}
print(id(n),id(o))


add=input("enter a value :")
print(add,type(add))
ad=eval(input("enter a value :"))
print(add,type(ad))