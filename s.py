marks=int(input("enter your marks"))
if    (marks>=90):
      Grade = 'A+'
elif  (marks<90 and marks>=80):
       Grade = 'A'
elif  (marks<80 and marks>=70):
       Grade = 'B+'
elif  (marks<70 and marks>=60):
       Grade = 'B'
elif  (marks<60 and marks>=50):
       Grade = 'C'
else  :
       Grade = 'D'
       
print ("Grade Of Student is", Grade)
a=input("enter your marks:")
print (type(a))
