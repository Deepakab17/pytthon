def data():
    for i in range(1,10):
        yield i
x = data()
print(next(x))
print(next(x))
print(next(x))
print("hello")
for i in x:
    print(i)
print(next(x))