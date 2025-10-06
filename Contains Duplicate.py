#Problem: Contains Duplicate
#Difficulty: Easy
#Link: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = {}
        # loop through all the nums
        for i in nums:
            if i in duplicate:
                return True 
            else: 
                duplicate[i] = True
        return False