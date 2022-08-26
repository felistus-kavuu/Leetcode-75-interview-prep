Bottom up approach:

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two= 1,1
        for i in range(0,n-1):
                temp= two
                two= one+two
                one= temp
        return two
        
        
        
 Top down approach: recurssion
 
