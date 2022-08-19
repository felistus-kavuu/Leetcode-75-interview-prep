#hashmap: counting frequency
#A hashmap is formed when only one of the counts of the elements is odd
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c= {}
        for char in s:
            if char not in c:
                c[char]=1
            else:
                c[char] +=1
        res=0
        odd=0
        
        if len(s)==1:
            return 1
        
        for i in c.values():
            if i>1:
                if(i%2==0):
                    res+=i
                else:
                    res+=i-1
                    odd+=1
            else:
                odd+=1
        
        if odd>0:
            res+=1
        
        return res
                
                
