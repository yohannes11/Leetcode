class Solution(object):
    def rob(self, nums):
        """
        [2,1,1,2]
               
                  
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <=2:
            return max(nums)
        memo = {0:nums[0],1: max(nums[:2])}
        for i in range(2,n):
            memo[i] = max(memo[i-1],nums[i]+memo[i-2])
            print(i)
            print(memo)
       
        return memo[n-1]
            
            
        