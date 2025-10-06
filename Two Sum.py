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
        map = {}
        # loop through the list
        for i in range(len(nums)):
            # Store the index 
            num = nums[i]
            # Equation to find the target value
            needed = target - nums[i]
            # If the needed number is in map return the vaule
            if needed in map:
                return[map[needed], i]
            # else store it in map
            else: 
                # Store num and index into map 
                map[num] = i 


if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result) 
    
