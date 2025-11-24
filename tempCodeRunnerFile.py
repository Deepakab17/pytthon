def natural(n):
    if n==1:
        print(1)
        return 
    natural(n-1)
    print(n)
natural(10)