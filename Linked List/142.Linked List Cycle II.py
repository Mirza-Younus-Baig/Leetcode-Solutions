from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = prev = head
        while cur and cur.next:
            cur = cur.next.next
            prev = prev.next
            if cur == prev:
                break
        else:
            return None
            
        cur = head
        while cur != prev:
            cur = cur.next
            prev=prev.next
        
        return prev
        