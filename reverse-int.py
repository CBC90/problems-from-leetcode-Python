# Given a 32-bit signed integer, reverse digits
class Solution:
    def reverse(self, x: int) -> int:
        
        # calculate the length of the input
        y = abs(x)
        length = len(str(y))
        
        if x == 0:
            return x
        
        # build new integer
        xinv = '0'
        for i in range(length):
            lastdig = y % 10
            y = int(y / 10)
            xinv = xinv + str(lastdig) 
        
        if x > 0:
            xinv = int(xinv)
        elif x < 0:
            xinv = -int(xinv)
        
        # if integer is larger than 32-bit, return 0
        if xinv > 2147483647:
            return 0
        elif xinv < -2147483648:
            return 0
        else:     
            return xinv
