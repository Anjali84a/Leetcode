# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr[left-1:right] = arr[left-1:right][::-1]
        new_node=ListNode(0)
        curr=new_node
        for val in arr:
            curr.next=ListNode(val)
            curr=curr.next
        return new_node.next
            
                

        