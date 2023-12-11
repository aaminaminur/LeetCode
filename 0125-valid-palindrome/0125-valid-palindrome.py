class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalnum(c: chr)-> bool:
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('0')<= ord(c) <= ord('9') or 
                    ord('a')<= ord(c) <= ord('z'))
        
        left = 0
        right = len(s) - 1
        while left <= right:
            if not isalnum(s[left]):
                left += 1
                continue
            if not isalnum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True