a=input("enter the name")
s=len(a)
n=(len(a)-1)//2
print(a[n])
for x in range(n,0,-1):
    for y in range(x+1,0,-1):
        print(a[y],end=" ")