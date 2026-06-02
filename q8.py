n=int(input("enter number"))
b=0
a=0
while n>0:
    c=n-((n//10)*10)
    a=a*10 + c
    b= b+ c*10
    n=n//10
print(b)