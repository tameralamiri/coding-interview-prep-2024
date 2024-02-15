# Trees:
# Trees are a collection of nodes, where each node has a value and a list of references to other nodes (children).
# They are used to represent hierarchical data.
# They are used to represent different data types:
# 1. File Systems: Trees are used to represent file systems as a collection of directories and files.
# 2. Organization Structure: Trees are used to represent organization structure as a collection of departments and employees.
# 3. HTML DOM: Trees are used to represent HTML DOM as a collection of elements and attributes.
# 4. Decision Trees: Trees are used to represent decision trees as a collection of nodes and edges.

# Tree Terminology:
###################
# 1. Node: each element in a tree.
# 2. Root: the topmost node in a tree.
# 3. Edge: the link between two nodes.
# 4. Parent: a node that has children.
# 5. Child: a node that has a parent.
# 6. Leaf: a node that has no children.
# 7. Sibling: nodes that share the same parent.
# 8. Depth: the length of the path from the root to a node.
# 9. Height: the length of the longest path from a node to a leaf.
# 10. Level: the depth of a node.
# 11. Degree: the number of children a node has.
# 12. Subtree: a tree within a tree.
# 13. Forest: a collection of trees.

# Main Types of Trees:
#################
# 1. Binary Tree: each node has at most two children.
# 2. Binary Search Tree (BST): a binary tree with the following properties:
#    - The left subtree of a node contains only nodes with keys less than the node's key.
#    - The right subtree of a node contains only nodes with keys greater than the node's key.
#    - The left and right subtree must also be a binary search tree.
# 3. Balanced Tree: designed to maintain a balance between the height of the left and right sub
# 4. B-Tree: a self-balancing search tree that can have more than two children.

# Tree Operations:
#################
# 1. Insertion: O(log n)
# 2. Deletion: O(log n)
# 3. Traversal: O(n) # Depth-First Traversal: Preorder, Inorder, Postorder, Breadth-First Traversal: Level Order
# 4. Search: O(log n)
# 5. Update: O(log n)

# Binary Tree Implementation:
# ###########################
# 1. Array Representation for Binary Tree:
#   - The root is at index 0.
#   - The left child of a node at index i is at index 2i + 1.
#   - The right child of a node at index i is at index 2i + 2.
#   - The parent of a node at index i is at index (i - 1) / 2.
#   - It's not efficient for sparse trees (trees with many null nodes).
#   - It's efficient for complete binary trees, heap data structure, and priority queues.
tree = ["A", "B", "C", "D", "E", "F", "G"]
# A: root, B: left child, C: right child, D: left child of B, E: right child of B, F: left child of C, G: right child of C

# 2. Adjacency List Representation for Binary Tree:
#   - Using a dictionary of lists to represent a binary tree.
#   - Each key in the dictionary represents a node.
#   - Each element in the list of that key represents the children of that node.
#   - It's efficient for sparse trees. and directed acyclic graphs. (DAGs)
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}
tree = [[1, 2], [3, 4], [5, 6], [], [], [], []]
# 0: root, 1: left child, 2: right child, 3: left child of 1, 4: right child of 1, 5: left child of 2, 6: right child of 2

# 3. Using User-Defined Class for Binary Search Tree:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    # Insertion, O(log n)
    def insert(self, value) -> None:
        if not self.root:
            self.root = TreeNode(value)
            return
        else:
            self._insert(self.root, value)
    def _insert(self, current_node, value):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = TreeNode(value)
            else:
                self._insert(current_node.left, value)
        else:
            if not current_node.right:
                current_node.right = TreeNode(value)
            else:
                self._insert(current_node.right, value)
    
    # Search, O(log n)
    def search(self, value) -> bool:
        return self._search(self.root, value)
    
    def _search(self, current_node, value):
        if not current_node:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)
        
    # Deletion, O(log n)
    def delete(self, value) -> None:
        self.root = self._delete(self.root, value) # Return the new root

    def _delete(self, current_node, value):
        if not current_node:
            return current_node
        if value < current_node.value:
            current_node.left = self._delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete(current_node.right, value)
        else: # Node to be deleted is found value == current_node.value
            if not current_node.left: # Node with only right child or no child
                temp = current_node.right
                current_node = None # Delete the node
                return temp # Return the right child
            
            elif not current_node.right: # Node with only left child
                temp = current_node.left
                current_node = None # Delete the node
                return temp # Return the left child
            else: # Node with two children
                temp = self._min_value_node(current_node.right) # Find the inorder successor (smallest in the right subtree)
                current_node.value = temp.value # replace the value of the current node with that of the inorder successor
                current_node.right = self._delete(current_node.right, temp.value) # Delete the inorder successor
        return current_node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current # Return the node with the minimum value
    
    # Update, O(log n)
    def update(self, old_value, new_value) -> str:
        if self.delete(old_value):
            self.insert(new_value)
        else:
            return "Value not found"
    
    # Traversal, O(n)
    # Depth-First Traversal: Preorder, Inorder, Postorder
    # Breadth-First Traversal: Level Order
    # pre-order: root -> left -> right
    def preorder_traversal(self):
        nodes = []
        self._preorder_traversal(self.root, nodes)
        print(nodes)

    def _preorder_traversal(self, current_node, nodes):
        if current_node:
            nodes.append(current_node.value)
            self._preorder_traversal(current_node.left, nodes)
            self._preorder_traversal(current_node.right, nodes)

    # in-order: left -> root -> right
    def inorder_traversal(self):
        nodes = []
        self._inorder_traversal(self.root, nodes)
        print(nodes)

    def _inorder_traversal(self, current_node, nodes):
        if current_node:
            self._inorder_traversal(current_node.left, nodes)
            nodes.append(current_node.value)
            self._inorder_traversal(current_node.right, nodes)

    # post-order: left -> right -> root
    def postorder_traversal(self):
        nodes = []
        self._postorder_traversal(self.root, nodes)
        print(nodes)

    def _postorder_traversal(self, current_node , nodes):
        if current_node:
            self._postorder_traversal(current_node.left, nodes)
            self._postorder_traversal(current_node.right, nodes)
            nodes.append(current_node.value)

    # level-order: top to bottom, left to right
    def level_order_traversal(self):
        if not self.root:
            return None
        nodes = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            nodes.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        print(nodes)

    # Balance a Tree:
    def balance(self) -> bool:
        # Store in-order traversal in a list
        in_order = []
        self._inorder_traversal(self.root, in_order)

        # Build a balanced tree from the list
        self.root = self._build_tree(in_order, 0, len(in_order) - 1)
    
    def _build_tree(self, in_order, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(in_order[mid])
        node.left = self._build_tree(in_order, start, mid - 1)
        node.right = self._build_tree(in_order, mid + 1, end)
        return node
    # height of a tree
    def height(self) -> int:
        return self._height(self.root)
    def _height(self, node):
        if not node:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        print(1 + max(left_height, right_height))
        return 1 + max(left_height, right_height)
    

# Binary Search Tree Operations:
###############################
bst = BinarySearchTree(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(5)
bst.insert(7)
#    4
#  2   6
# 1 3 5 7
bst.preorder_traversal() # [4, 2, 1, 3, 6, 5, 7]
bst.inorder_traversal() # [1, 2, 3, 4, 5, 6, 7]
bst.postorder_traversal() # [1, 3, 2, 5, 7, 6, 4]
bst.level_order_traversal() # [4, 2, 6, 1, 3, 5, 7]

# Balancing a Tree:
bst2 = BinarySearchTree(10)
bst2.insert(8)
bst2.insert(4)
bst2.insert(2)
bst2.insert(1)
bst2.insert(11)
#      10
#    8  11
#  4
# 2
#1       
bst2.preorder_traversal() # [10, 8, 4, 2, 1, 11]
print(bst2.height())
bst2.balance()
#   4
# 2    10
#1    8  11
bst2.preorder_traversal() # [4, 2, 1, 10, 8, 11]
print(bst2.height())


