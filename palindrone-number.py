# Determines whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        ans = False
        y = str(x)
        
        for i in range(len(y)):
            if y[i] == y[len(y) - 1 - i]:
                ans = True
            elif y[i] != y[len(y) - 1 - i]:
                return False
        return ans
        
