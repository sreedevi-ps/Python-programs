

def max_num():
  num=[-2,1,-3,4,-1,2,1,-5,4]
  max_sum=num[0]
  current_sum=num[0]
  for i in range (1,len(num)):
    current_sum=max(num[i],current_sum+num[i])
    max_sum=max(max_sum,current_sum)
  return (max_sum)
k=max_num()
print(k)