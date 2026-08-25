# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        new_node=ListNode(0)
        curr=new_node
        for val in arr:
            curr.next=ListNode(val)
            curr=curr.next
        return new_node.next
        