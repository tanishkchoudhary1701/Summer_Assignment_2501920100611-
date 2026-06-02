n=int(input("enter number"))
a=1
while n>0:
    b=n//10
    c=n-(b*10)
    a*=c
    n=n//10
print(a)