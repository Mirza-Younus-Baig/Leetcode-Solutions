from typing import Optional

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(data)

    def display(self):
        cur_node = self.head.next
        while cur_node:
            print(cur_node.data, end = " ")
            cur_node = cur_node.next
        print()
    

class Solution:
    def reverseList(self, head: Node) -> Node:
        prev, cur_node = None, head
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = temp

        return self.display(prev)
    
    def display(self, head: Node) -> list:
        cur_node = head
        elem = []
        while cur_node.next:
            elem.append(cur_node.data)
            cur_node = cur_node.next
        return elem
    


if __name__ == "__main__":

    # Creating sample linked list for input
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.display()

    # Reversing the linked list
    res = Solution()
    print(res.reverseList(ll.head))
    