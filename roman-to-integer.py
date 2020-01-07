# Translates a Roman number of user input into an integer

class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        c = 0
        
        while c < len(s):
            if s[c:c + 2] == "IV":
                x = x + 4
                c = c + 1
            elif s[c:c + 2] == 'IX':
                x = x + 9
                c = c + 1
            elif s[c:c + 2] == 'XL':
                x = x + 40
                c = c + 1
            elif s[c:c + 2] == 'XC':
                x = x + 90
                c = c + 1
            elif s[c:c + 2] == 'CD':
                x = x + 400
                c = c + 1
            elif s[c:c + 2] == 'CM':
                x = x + 900
                c = c + 1
            elif s[c:c + 1] == 'I' and (s[c + 1: c + 2] != 'V' or s[c + 1: c + 2] != 'X'):
                x = x + 1
            elif s[c:c + 1] == 'V':
                x = x + 5
            elif s[c:c + 1] == 'X' and (s[c + 1: c + 2] != 'L' or s[c + 1: c + 2] != 'C'):
                x = x + 10
            elif s[c:c + 1] == 'L':
                x = x + 50
            elif s[c:c + 1] == 'C' and (s[c + 1: c + 2] != 'D' or s[c + 1: c + 2] != 'M'):
                x = x + 100
            elif s[c:c + 1] == 'D':
                x = x + 500
            elif s[c:c + 1] == 'M':
                x = x + 1000
            c = c + 1
        return x
