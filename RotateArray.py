# 189. Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:

# TODO: Could you do it in-place with O(1) extra space?

# Time limit exceeded first solution.
class BadSolution:
    def rotate(self, nums, k):
        for _ in range(1,k+1):
            for i in range(1, len(nums)):
                nums[0], nums[i] = nums[i], nums[0]

# my solution
class Solution:
    def rotate(self, nums, k):
        arr = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            target = (i+k) % len(nums)
            arr[target] = nums[i]

        for i in range(len(nums)): nums[i] = arr[i]
                
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums,3)
print(nums)