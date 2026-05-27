class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # XOR cancels duplicate numbers and leaves the single unique number
        # Time complexity: O(n) only one pass
        # Space Complexity: O(1) one variable
        result = 0
        for num in nums:
            result ^= num
        return result 