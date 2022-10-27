class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(i,curr,current_sum):
            if i >= n or current_sum > target:
                return
            
            if current_sum == target:
                res.append(curr.copy())
                return
            curr.append(candidates[i])
            backtrack(i,curr,current_sum+candidates[i])
            curr.pop()
            backtrack(i+1,curr,current_sum)
        backtrack(0,[],0)  
        return res
            
            
            