class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <=2:
            return max(nums)
        memo = {0:nums[0],1: max(nums[:2])}
        for i in range(2,n):
            memo[i] = max(memo[i-1],nums[i]+memo[i-2])
        return memo[n-1]
            
            
        