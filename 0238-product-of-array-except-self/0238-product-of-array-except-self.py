import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for i in range(n)]
        postfix = [1 for i in range(n)]
        res = [1] * n
        curr_prefix = 1
        curr_postfix = 1
        
        for i in range(n-1):           
            curr_prefix = curr_prefix * nums[i]
            prefix[i+1] = curr_prefix
    
    
        for j in range(n-1,0,-1):           
            curr_postfix = curr_postfix * nums[j]
            postfix[j-1] = curr_postfix
        print(postfix)
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        
        return res
        
        