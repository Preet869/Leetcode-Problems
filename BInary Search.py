class Solution(object):
    def search(self, nums, target):
        # Start by halving the nums to find the middle
        # if the target is found then end 
        # if not then half the list 
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1 

            else:
                high = mid - 1
        return - 1

    # When to use Binary Search - When the array is sorted, need to find the target, can eliminate half each step.