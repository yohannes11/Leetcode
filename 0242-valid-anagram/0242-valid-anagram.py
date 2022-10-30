from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for s_value in s:
            s_dict[s_value]+=1
        
        for t_value in t:
            t_dict[t_value]+=1
            
        for s_value in s_dict:
            if t_dict[s_value] != s_dict[s_value]:
                return False
        for t_value in t_dict:
            if s_dict[t_value] != t_dict[t_value]:
                return False
        print(t_dict)
        print(s_dict)
        return True
            
        
        