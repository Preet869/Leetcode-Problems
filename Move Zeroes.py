# 283. Move Zeroes
#Problem: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0  # This will point to the position where the next non-zero element should go

        # 1. First pass: move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # 2. Second pass: fill the remaining positions with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        return insert_pos
