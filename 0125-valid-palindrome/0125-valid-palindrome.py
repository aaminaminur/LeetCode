import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        asciilist = [ord('a')]
        for i in range(1, 26):
            asciilist.append(ord('a')+i)
        for i in range(0,10):
            asciilist.append(ord('0')+i)
        left = 0
        right = len(s)-1
        while(left<right):
            if ord(s[left]) not in asciilist:
                left += 1
                continue
            if ord(s[right]) not in asciilist:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True