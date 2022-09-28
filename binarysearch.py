#Operation:
 # 1. Works with sorted elements
  #2. Start with the middle of the element as a reference
  #3. Check the middle of the element againsta the required element
   #   -If it is greater than the required element it means we don't need to search in the first half -If it is less than then we only continue searching for our element in the first half
 

Iterative approach:
  class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        #O(n) time complexity
        l,r=0,n-1
        
        while(r-l)>1:
            mid= (r+l)//2
            if (nums[mid]<target):
                l= mid+1
            else:
                r= mid
        
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        else:
            return -1
            
Recurssive approach:
  
