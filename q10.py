n=int(input("enter range"))
print(2)
for i in range(3,n+1):
    for j in range(2,int(i/2+1)):
        if i%j==0:
            break
    else:
        print(i)
