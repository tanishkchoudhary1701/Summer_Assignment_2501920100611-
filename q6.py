n=int(input("enter number"))
a=0
while n>0:
    c=n-((n//10)*10)
    a=a*10 + c
    n=n//10
print(a)