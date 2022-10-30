class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        sum_dict = {2:0,7:1}
        
        '''
        sum_dict = {}
        
        for i in range(len(nums)):
            if target-nums[i] in sum_dict:
                return [i,sum_dict[target-nums[i]]]
            sum_dict[nums[i]] = i 
                
                
            
                
            
        