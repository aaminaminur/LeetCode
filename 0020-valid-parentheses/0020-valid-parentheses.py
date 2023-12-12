class Solution:
    def isValid(self, s: str) -> bool:
        choices = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for ch in s:
            if stack and ch in choices:
                if stack[-1] != choices[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        
        return False if stack else True