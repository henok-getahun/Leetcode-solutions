# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode(0)
        prev=head
        carry=0
        while l1 and l2:
            sum_val = carry + l1.val + l2.val
            carry = sum_val // 10
            curr = ListNode(sum_val % 10)
            prev.next = curr
            prev = curr
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_val = carry + l1.val
            carry = sum_val // 10
            curr = ListNode(sum_val % 10)
            prev.next = curr
            prev = curr
            l1 = l1.next

        while l2:
            sum_val = carry + l2.val
            carry = sum_val // 10
            curr = ListNode(sum_val % 10)
            prev.next = curr
            prev = curr
            l2 = l2.next
        
        if carry != 0:
            prev.next = ListNode(carry)

        
        

        return head.next







