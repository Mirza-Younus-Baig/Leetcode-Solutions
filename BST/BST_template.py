class Node:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

# Define class bst and implement insert method

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)
    
    def _add(self, value, current):
        if value < current.value:
            if current.left == None:
                current.left = Node(value)
            else:
                self._add(value, current.left)
        else:
            if current.right == None:
                current.right = Node(value)
            else:
                self._add(value, current.right)

    def preorder(self):
        if self.root:
            self._preorder(self.root)
        print()
    
    def _preorder(self, node):
        if node:
            print(node.value, end = "  ")
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self):
        if self.root:
            self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end = "  ")
            self._inorder(node.right)

    def postorder(self):
        if self.root:
            self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end = "  ")

# class BST:

#     def __init__(self):
#         self.root = None
    
#     def add(self, val):
#         if self.root is None:
#             self.root = Node(val)
#         else:
#             self._add(val, self.root)
    
#     # Implement recursive add method
#     def _add(self, val, node):
#         if val < node.val:
#             if node.left is None:
#                 node.left = Node(val)
#             else:
#                 self._add(val, node.left)
#         else:
#             if node.right is None:
#                 node.right = Node(val)
#             else:
#                 self._add(val, node.right)
    
#     # Implment search method
#     def find(self, val):
#         if self.root:
#             is_found = self._find(val, self.root)
#             if is_found:
#                 return True
#             return False
#         else:
#             return None
    
#     # Implement recursive search method
#     def _find(self, val, node):
#         if val > node.val and node.right:
#             return self._find(val, node.right)
#         elif val < node.val and node.left:
#             return self._find(val, node.left)
#         if val == node.val:
#             return True
    
#     # Implement traversal methods
#     def preorder(self):
#         if self.root:
#             self._preorder(self.root)

#     def _preorder(self, node):
#         if node:
#             print(str(node.val))
#             self._preorder(node.left)
#             self._preorder(node.right)
    
#     def inorder(self):
#         if self.root:
#             self._inorder(self.root)
    
#     def _inorder(self, node):
#         if node:
#             self._inorder(node.left)
#             print(str(node.val))
#             self._inorder(node.right)
    
#     def postorder(self):
#         if self.root:
#             self._postorder(self.root)
    
#     def _postorder(self, node):
#         if node:
#             self._postorder(node.left)
#             self._postorder(node.right)
#             print(str(node.val))
    
#     # Implement delete method
#     def delete(self, val):
#         if self.root:
#             self.root = self._delete(val, self.root)
    
#     def _delete(self, val, node):
#         if node is None:
#             return node
#         if val < node.val:
#             node.left = self._delete(val, node.left)
#         elif val > node.val:
#             node.right = self._delete(val, node.right)
#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             else:
#                 temp = self.find_min(node.right)
#                 node.val = temp.val
#                 node.right = self._delete(temp.val, node.right)
#         return node
    
                          


if __name__ == "__main__":
    bst = BST()
    bst.add(10)
    bst.add(4)
    bst.add(15)
    bst.add(12)
    bst.add(2)
    bst.add(7)

    bst.preorder()
    bst.inorder()
    bst.postorder()