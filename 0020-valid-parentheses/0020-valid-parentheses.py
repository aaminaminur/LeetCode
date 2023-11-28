class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if stack and ch in CloseToOpen:
                if stack[-1] == CloseToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False