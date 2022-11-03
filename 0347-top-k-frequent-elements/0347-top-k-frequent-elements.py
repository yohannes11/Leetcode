from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)    
        output_array = []
        for num in nums:
            nums_dict[num]+=1
        unique_keys = list(nums_dict.values())
        unique_keys.sort(reverse=True)
        unique_keys = unique_keys[:k]
        print(unique_keys)
        for current_key in nums_dict:
            if nums_dict[current_key] in unique_keys:
                output_array.append(current_key)
        
        return output_array
            
        
        