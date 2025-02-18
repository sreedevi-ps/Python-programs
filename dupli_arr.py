class Solution(object):
    def containsDuplicate(self, nums):
      new_nums=[]
      for num in nums:
        if(num in new_nums):
            return True
        new_nums.append(num)
      return False
s=Solution()
nums=[]
for i in range(5):
   a=int(input(f"enter element"))
   nums.append(a)
k=s.containsDuplicate(nums)
print("presence of duplicate:",k)