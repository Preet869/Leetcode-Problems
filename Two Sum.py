# Two Sum
#Problem: Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to the target.
#Topcis
    # Hashmaps
    # Arrays & Indexing
    # Enumerate

#Solution:
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums): # for i in range(len(nums)):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result) 
    
