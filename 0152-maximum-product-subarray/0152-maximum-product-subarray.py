class Solution(object):
    def maxProduct(self, nums):
#         res = nums[0]
#         max_product, min_product = 1,1

#         for num in nums:
#             tmp = max_product * num
#             max_product = max(max_product * num, min_product*num, num)
#             min_proudct = min(tmp, min_product*num, num)
#             res= max(max_product,res)
#         return res
    # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
        
        
            
        
        