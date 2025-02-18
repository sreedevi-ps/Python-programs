'''Problem Statement
You are given an integer array nums where each element represents your maximum jump length at that position. Your goal is to determine if you can reach the last index starting from the first index.

Example
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index1.'''

def canJump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

# Example usage:
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

print(canJump(nums1))  # Output: True
print(canJump(nums2))  # Output: False









