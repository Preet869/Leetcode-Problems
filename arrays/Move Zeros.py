class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        non_zero_pos = 0
        if not nums:
            return 0

        while i < len(nums):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1
            i += 1

        while non_zero_pos < len(nums):
            nums[non_zero_pos] = 0
            non_zero_pos += 1

        return nums
