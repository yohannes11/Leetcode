class Solution(object):
    def maxProduct(self, nums):
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            
            tmp = curMax * num
            curMax = max(num * curMax, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res= max(res,curMax)
        return res
        
        
            
        
        