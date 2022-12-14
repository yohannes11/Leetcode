class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        self.max_substring = s[0]
        if n <=1:
            return s[0]
        
        def helper(left_pointer, right_pointer,current_substring):
            while left_pointer >=0 and right_pointer<n:
                if s[left_pointer]==s[right_pointer]:
                    current_substring = s[left_pointer]+current_substring+s[right_pointer]
                else:
                    break
                if len(current_substring) > len(self.max_substring):
                    self.max_substring = current_substring
                left_pointer-=1
                right_pointer+=1
         
        for i in range(len(s)):
            left_pointer = i-1
            right_pointer = i+1
            current_substring = s[i]
            helper(left_pointer,right_pointer,current_substring)
            
                
            left_pointer = i-1
            right_pointer = i+2
            if i+1 < n and s[i]==s[i+1]:
                current_substring = s[i:i+2]
                if len(current_substring) > len(self.max_substring):
                    self.max_substring = current_substring
                helper(left_pointer,right_pointer,current_substring)
                
                
        return self.max_substring
              
                
            
        