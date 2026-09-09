from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        queue=deque()
        while slow:
            queue.append(slow.val)
            slow=slow.next
        slow=head
        sum=0
        while queue:
            x=slow.val
            y=queue.pop()
            sum=max(sum,x+y)
            slow=slow.next
        return sum
