# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp1=list1
        temp2=list2
        while temp1:
            arr.append(temp1.val)
            temp1=temp1.next
        while temp2:
            arr.append(temp2.val)
            temp2=temp2.next
        arr.sort()
        curr=ListNode(0)
        new_node=curr
        for val in arr:
            curr.next=ListNode(val)
            curr=curr.next
        return new_node.next

        