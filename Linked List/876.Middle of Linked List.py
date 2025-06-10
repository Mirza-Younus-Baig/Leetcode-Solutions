# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lenLL = 0
        while temp:
            lenLL += 1
            temp = temp.next
        
        lenLL = lenLL // 2
       
        
        temp = head
        while lenLL:
            lenLL -= 1
            temp = temp.next
        
        return temp
