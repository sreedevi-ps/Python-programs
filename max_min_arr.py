n=int(input("enter array size"))
a=[]
max=0
min=100000
for i in range(n):
    elements=int(input("enter elements"))
    a.append(elements)
    print(a)
    if(a[i]>max):
        max=a[i]
    if(a[i]<min):
        min=a[i]
print("max element is",max)
print("min element is",min)
