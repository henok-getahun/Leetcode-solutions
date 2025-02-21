# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       if not lists or len(lists) ==0:
            return None

       while len(lists) > 1:
            mergedLists=[]
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append( self.mergeLists(list1,list2))
            lists = mergedLists
        
       return lists[0]


    def mergeLists(self, list1, list2):
        dummyNode=ListNode()
        current = dummyNode
        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        if list2:
            current.next=list2
        return dummyNode.next




