n=int(input("enter n as limit"))
f1=0
f2=1
print(f1,end=" ")
print(f2,end=" ")
while(True):
 f3=f1+f2
 if(f3>n):
  break
 print(f3,end=" ")
 f1=f2
 f2=f3



    