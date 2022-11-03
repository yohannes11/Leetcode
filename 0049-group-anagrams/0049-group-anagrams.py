class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = {}   
        for value in strs:
            key = ''.join(sorted(list(value)))
            if key in anagram_dict:
                anagram_dict[key].append(value)
            else:
                anagram_dict[key] = [value]
        return anagram_dict.values()
                
                
        
        