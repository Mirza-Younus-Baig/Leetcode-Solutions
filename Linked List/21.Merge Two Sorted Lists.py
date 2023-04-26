# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def display(self, node):
        print()
        while node:
            print(node.val)
            node = node.next


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        res = ListNode()
        reshead = res
        while l1 and l2:
            node = ListNode(val = (l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10

            reshead.next = node
            
            reshead = reshead.next

            # self.display(res)

            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                node = ListNode(val = (l1.val + carry)%10)
                carry = (l1.val + carry)//10

                reshead.next = node
                
                reshead = reshead.next
                l1 = l1.next
        elif l2:
            while l2:
                node = ListNode(val = (l2.val + carry)%10)
                carry = (l2.val + carry)//10

                reshead.next = node
                
                reshead = reshead.next
                l2 = l2.next

        if carry:
            reshead.next = ListNode(val = carry)
            reshead = reshead.next

        return res.next
