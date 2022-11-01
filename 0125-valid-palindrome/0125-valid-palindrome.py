class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([s[i].lower() for i in range(len(s)) if s[i].isalnum()])
        left_ptr, right_ptr = 0, len(s) - 1  
        while left_ptr<= right_ptr:
            if s[left_ptr]!=s[right_ptr]:return False
            left_ptr+=1
            right_ptr-=1
        return True
                
        