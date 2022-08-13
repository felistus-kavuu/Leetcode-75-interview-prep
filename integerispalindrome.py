Approach one:
  Obtain the reverse of the number then compare the reverse with the number that you have with the formula below
  reversed= reversed*10 + x%10
  x=x//10
  
  then compare the two
  Remember to store the original value of x before you begin manipulation
  
  class Solution:
    def isPalindrome(self, x: int) -> bool:
        #x= str(x)
        if x<0:
            return False
        
        original=x
        revers=0
        
        while x>0:
            revers=revers*10+x%10
            x=x//10
            
        if revers==original:
            return True
          
  Approach two:
    Convert the integer into a string
    Split the string into half and compare both halves
    
    
    
    class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        z= str(x)
        
        if(z == z[::-1]):
            return True
