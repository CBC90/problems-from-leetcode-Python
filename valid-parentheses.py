# Determines the validity of a user-input set of parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        
        par = ['(', ')', '[', ']', '{', '}']
        i = -1
        
        if len(s) == 0:
            return True
        
        if (len(s) % 2) != 0:
            return False
        
        stack = [0] * len(s)
        
        for char1 in s:
            i += 1
            j = -1
            for char2 in par:
                j += 1
                if char1 == char2:
                    stack[i] = j
                    break
        if stack[0] % 2 != 0:
            return False

        x = 1
        y = len(stack)
        while x < y:
            if stack[x] == stack[x - 1] + 1:
                stack.pop(x)
                stack.pop(x - 1)
                x = 0
                y = len(stack)
            x += 1
        if len(stack) == 0:
            return True

        else:
            return False
