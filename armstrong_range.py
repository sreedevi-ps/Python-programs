n=int(input("enter limit"))
for n in range(1,n+1):
    temp=n
    arm=0
    while temp>0:
        d=temp%10
        arm+=d**3
        temp=temp//10
    if(arm==n):
        print(arm,"is a armstrong no.")