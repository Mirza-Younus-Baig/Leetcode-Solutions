# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Operations:
    def __init__(self):
        self.head = ListNode()

    def append(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val=val)
    
    def display(self):
        curr = self.head
        while curr.next:
            print(curr.next, "->", end = "")
            curr = curr.next
        print(curr.next)


class Solution:
    def isPalindrome(self, head: Operations) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True


if __name__ == "__main__":
    myList = Operations()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(2)
    myList.append(1)
    
    myList.display()

    res = Solution()
    print(res.isPalindrome(myList))