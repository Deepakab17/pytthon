# def decorator(x):
#     def inner(p,q,r):
#         p=p+5
#         q=q+10
#         r=r+15
#         z=x(p,q,r)
#         return z
#     return inner
# @ decorator
# def add(a,b,c):
#     return a+b+c
# res=add(2,4,6)
# print(res)
def decorator(func):
    def inner(p, q, r):  
        p = p - 1
        q = q + 1
        return func(p, q, r)  
    return inner

@decorator
def even_no(p, q, r):
    for i in range(p, q, r):
        if i % 2== 0:
            print(i)

even_no(2, 101, 1)

