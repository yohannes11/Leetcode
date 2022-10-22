class Solution(object):
    def maxProduct(self, nums):
        res = nums[0]
        min_product, max_product = 1, 1

        for num in nums:
            
            tmp = max_product * num
            max_product = max(num * max_product, num*min_product, num)
            min_product = min(tmp, num*min_product, num)
            res= max(res,max_product)
        return res
        
        
            
        
        