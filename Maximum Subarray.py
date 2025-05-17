#Problem: Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Algorithm: Kadane’s Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            # Decide to add to current or start fresh
            current_sum = max(num, current_sum + num)

            # Update max if current is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
    
