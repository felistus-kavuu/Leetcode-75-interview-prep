Reverese a linked list
Given the head of a singly linked list, reverse the list, and return the reversed list.
Iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr= head
        
        while curr:
            temp= curr.next
            curr.next= prev
            prev= curr
            curr= temp
            
        return prev
        
Recursive approach:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        
        newHead= self.reverseList(head.next)
        head.next.next= head
        head.next= None
        
        return newHead
