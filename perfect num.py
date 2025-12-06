n=int(input("enter the number"))
pertotal=0
for i in range(1,n):
    if n%i==0:
        print(i)
        pertotal=pertotal+i
print(pertotal)
        