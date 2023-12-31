class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfDigits(n)
                
            if n == 1:
                return True
        
        return False
    
    def sumOfDigits(self, n: int) -> int:
        
        output = 0
        
        while n:
            digit = n%10
            output += (digit*digit)
            n = n//10
        
        return output