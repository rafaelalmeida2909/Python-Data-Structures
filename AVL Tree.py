class Node:
    """Class to represent a node in Python3"""

    def __init__(self, data):
        self.data = data  # Node value
        self.left = None  # Left node
        self.right = None  # Right node
        self.parent = None  # Parent of node
        self.height = 1


class AvlTree:
    """Class to represent a AVL tree in Python3"""

    def __init__(self):
        self._root = None  # The root of tree
        self._nodes = 0  # Number of nodes

    def heightNode(self, node):
        """Returns the height of nodes"""
        if node is None:
            return 0
        else:
            return node.height

    def copy(self, node):
        """Copys the atributtes of a node to a new node and return it"""
        new = Node(node.data)
        new.left = node.left
        new.right = node.right
        new.parent = node.parent
        new.height = node.height
        return new

    def updateHeights(self, node):
        """Updates the height of nodes"""
        while True:
            if node is None:
                break
            node.height = max(self.heightNode(node.left),
                              self.heightNode(node.right)) + 1
            node = node.parent

    def balanceTree(self, node):
        """Tree balancing function"""
        while True:
            if node is None:
                break
            if self.balanceFactor(node) == -2:
                if self.balanceFactor(node.right) == 1:
                    self.rlRotation(node)
                else:
                    self.llRotation(node)
                break
            elif self.balanceFactor(node) == 2:
                if self.balanceFactor(node.left) == -1:
                    self.lrRotation(node)
                else:
                    self.rrRotation(node)
                break
            node = node.parent
        self.updateHeights(node)

    def balanceFactor(self, node):
        """Balancing factor function"""
        if node is None:
            return 0
        return self.heightNode(node.left) - self.heightNode(node.right)

    def returnNode(self, current):
        """Auxiliary method that return the node to be relocated"""
        if current.left == None:
            node2 = current.right
            return node2
        node1 = current
        node2 = current.left
        while node2.right != None:
            node1 = node2
            node2 = node2.right
        if node1 != current:
            node1.right = node2.left
            if node2.left != None:
                node2.left.parent = node1
            node2.left = current.left
            node1.parent = current.left
            node1.height = max(self.heightNode(node1.left),
                               self.heightNode(node1.right)) + 1
        node2.right = current.right
        if current.right != None:
            current.right.parent = node2
        if current.left != None:
            current.left.parent = node2
        if current == self._root:
            node2.parent = None
            self.balanceTree(node1)
        return node2

    def rrRotation(self, root):
        print("rr")
        """Right rotation function"""
        node = self.copy(root.left)
        root.left = node.right
        root.height = max(self.heightNode(root.left),
                          self.heightNode(root.right)) + 1
        node.right = self.copy(root)
        node.height = max(self.heightNode(node.left), root.height) + 1
        root.data = node.data
        root.left = node.left
        root.right = node.right
        root.height = node.height
        root.right.parent = root
        if root.right.left != None:
            root.right.left.parent = root.right
        if root.right.right != None:
            root.right.right.parent = root.right

    def llRotation(self, root):
        print("ll")
        """Left rotation function"""
        node = self.copy(root.right)
        root.right = node.left
        root.height = max(self.heightNode(root.left),
                          self.heightNode(root.right)) + 1
        node.left = self.copy(root)
        node.height = max(self.heightNode(node.right), root.height) + 1
        root.data = node.data
        root.left = node.left
        root.right = node.right
        root.height = node.height
        root.left.parent = root
        if root.left.right != None:
            root.left.right.parent = root.left
        if root.left.left != None:
            root.left.left.parent = root.left

    def lrRotation(self, node):
        """Left right rotation function"""
        self.llRotation(node.left)
        self.rrRotation(node)

    def rlRotation(self, node):
        """Right left rotation function"""
        self.rrRotation(node.right)
        self.llRotation(node)

    def insert(self, value):
        """Inserts a node by your value"""
        if self._root is None:
            self._root = Node(value)
            self._nodes += 1
        else:
            pointer = self._root
            while True:
                if pointer.data > value:
                    if pointer.left is None:
                        break
                    pointer = pointer.left
                elif pointer.data < value:
                    if pointer.right is None:
                        break
                    pointer = pointer.right
                else:
                    raise Exception("The node already exists")
            node = pointer
            if node.data > value:
                new = Node(value)
                node.left = new
                new.parent = node
                self._nodes += 1
                node = node.left
            else:
                new = Node(value)
                node.right = new
                new.parent = node
                self._nodes += 1
                node = node.right
            self.updateHeights(node)
            self.balanceTree(node)

    def heightsAfterRemoved(self, node):
        """Auxiliary function to update the height of nodes, after removing a node"""
        minim = self.min(node, False)
        maxim = self.max(node, False)
        self.updateHeights(minim)
        self.updateHeights(maxim)

    def balanceAfterRemoved(self, node):
        """Auxiliary function to verify balance factor of nodes, after removing a node"""
        minim = self.min(node, False)
        maxim = self.max(node, False)
        self.balanceTree(minim)
        self.balanceTree(maxim)

    def remove(self, value):
        """Removes a node and regroup the tree"""
        prev = None
        current = self._root
        while current != None:
            if value == current.data:
                if current == self._root:
                    self._root = self.returnNode(current)
                else:
                    if prev.right == current:
                        prev.right = self.returnNode(current)
                        if prev.right != None:
                            prev.right.parent = prev
                    else:
                        prev.left = self.returnNode(current)
                        if prev.left != None:
                            prev.left.parent = prev
            prev = current
            if value > current.data:
                current = current.right
            else:
                current = current.left
        if not self.empty():
            self.heightsAfterRemoved(prev.parent)
            self.balanceAfterRemoved(prev.parent)
        self._nodes -= 1

    def preOrder(self, node):
        """Prints the tree: root -> left node -> right node"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def order(self, node):
        """Prints the tree: left node -> root -> right node"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            self.order(node.left)
            print(node.data)
            self.order(node.right)

    def postOrder(self, node):
        """Prints the tree: left node -> right node -> root"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data)

    def search(self, value):
        """Returns true if the value is in the tree, otherwise, it returns false"""
        if self._root is None:
            raise Exception("The tree is empty")
        pointer = self._root
        while True:
            if pointer.data > value:
                if pointer.left is None:
                    return False
                pointer = pointer.left
            elif pointer.data < value:
                if pointer.right is None:
                    return False
                pointer = pointer.right
            else:
                return True

    def min(self, node=None, value=True):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        else:
            pointer = node
        while pointer.left:
            pointer = pointer.left
        if value:
            print(pointer.data)
        else:
            return pointer

    def max(self, node=None, value=True):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        else:
            pointer = node
        while pointer.right:
            pointer = pointer.right
        if value:
            print(pointer.data)
        else:
            return pointer

    def clear(self):
        """Restores the tree to its starting point (Empty)"""
        self._root = None
        self._nodes = 0

    def height(self, node):
        """Returns the tree's height"""
        if self._root is None:
            raise Exception("The tree is empty")
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            if (left_height > right_height):
                return left_height + 1
            else:
                return right_height + 1

    def nodes(self):
        """Returns the number of nodes in the tree"""
        return self._nodes

    def root(self):
        """Returns the tree's root node"""
        return self._root

    def empty(self):
        """Returns true if the tree is empty, otherwise, it returns false"""
        if self._root is None:
            return True
        return False

    def printTree(self, node=None):
        """Prints the Avl Tree"""
        if node is None:
            node = self._root
        lines, *_ = self._printTree(node)
        for line in lines:
            print(line)

    def _printTree(self, node):
        """Auxiliary function to print the Avl Tree"""
        if node.right is None and node.left is None:  # No child
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:  # Only left child
            lines, n, p, x = self._printTree(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left is None:  # Only right child
            lines, n, p, x = self._printTree(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._printTree(node.left)  # Two children
        right, m, q, y = self._printTree(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def printHeights(self):
        """Prints the height of nodes"""
        if self._root != None:
            print("Node, Height")
            self._printHeights(self._root)

    def _printHeights(self, cur_node):
        """Auxiliary function to print the height of nodes"""
        if cur_node != None:
            self._printHeights(cur_node.left)
            print(f'{cur_node.data},'.center(5) +
                  f' {str(cur_node.height).center(6)}')
            self._printHeights(cur_node.right)

    def printParents(self):
        """Prints the parent of nodes"""
        if self._root != None:
            print("Node, Parent")
            self._printParents(self._root)

    def _printParents(self, cur_node):
        """Auxiliary function to print the parent of nodes"""
        if cur_node != None:
            self._printParents(cur_node.left)
            if cur_node.parent != None:
                print(f'{cur_node.data},'.center(5) +
                  f' {str(cur_node.parent.data).center(6)}')
            else:
                print(f'{cur_node.data},'.center(5) +
                  f' {str(None).center(6)}')
            self._printParents(cur_node.right)
