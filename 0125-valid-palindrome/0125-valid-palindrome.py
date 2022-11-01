class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_str = ''.join([s[i].lower() for i in range(len(s)) if s[i].isalnum()])
        left_ptr, right_ptr = 0, len(output_str) - 1  
        while left_ptr<= right_ptr:
            if output_str[left_ptr]!=output_str[right_ptr]:return False
            left_ptr+=1
            right_ptr-=1
        return True
                
        