
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        self.head = Node()

    def append(self, data):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(data)
    
    def display(self):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            print(cur_node.data, end = " ")
        print()

    def length(self) -> int:
        cur_node = self.head
        length = 0
        while cur_node.next:
            cur_node = cur_node.next
            length += 1
        return length

    def get(self, index):
        if index >= self.length():
            return "Error: Index out of bounds"
        cur_node = self.head.next
        ind = 0
        while cur_node:
            if ind == index:
                return cur_node.data
            cur_node = cur_node.next
            ind += 1
        
    def delete(self, index):
        if index >= self.length():
            print("Error: Index out of bounds")
            return 
        cur_node = self.head
        ind = 0
        while True:
            if ind == index:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next
            ind += 1



myList = LinkedList()

myList.append(10)
myList.display()
print("Length of linked list", myList.length())
myList.append(15)
myList.display()
print("Length of linked list", myList.length())
myList.append(20)
myList.append(25)
myList.append(30)
myList.display()

myList.delete(0)
myList.display()

# implement searcing and deletion using value



