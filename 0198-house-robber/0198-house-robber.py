class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <=2:
            return max(nums)
        current = nums[0]
        current_max = max(nums[:2])
        for i in range(2,n):
            temp = current_max
            current_max = max(current_max,nums[i]+current)
            current = temp
        return current_max
            
            
        