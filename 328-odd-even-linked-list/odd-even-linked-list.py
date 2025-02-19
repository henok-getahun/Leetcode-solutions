# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead=head
        evenHead=head.next
        oddCurr=oddHead
        evenCurr=evenHead
        while evenCurr and evenCurr.next:
            oddCurr.next=evenCurr.next
            evenCurr.next=oddCurr.next.next
            oddCurr=oddCurr.next
            evenCurr=evenCurr.next
        
        if oddCurr:
            oddCurr.next=evenHead
        
        return head
        


        