Using memoization
        memo={}
        if n in memo:
            return memo[n]
        if n==0:
            memo[0]=0
            return 0
        if n==1:
            memo[1]=1
            return 1
        if n>1:
            memo[n]= self.fib(n-1)+self.fib(n-2)
            return memo[n]
Using recurssion:
  class Solution(object):
   # memo={}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+ self.fib(n-2)
      
 Iteratively:
  class Solution(object):
   # memo={}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev1, prev2=0,1
        output=0
        if n==0: return 0
        if n==1: return 1
        for i in range(2,n+1):
          output= prev1+prev2
          prev1=prev2
          prev2=output
          
        return output

