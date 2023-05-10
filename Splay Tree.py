class Node:
    """Class to represent a node in Python3"""

    def __init__(self, key):
        self.key = key  # Node value
        self.left = None  # Left node
        self.right = None  # Right node
        self.parent = None  # Parent node


class SplayTree:
    """Class to represent a splay tree in Python3"""

    def __init__(self):
        self._root = None  # The root of tree
        self._nodes = 0  # Number of nodes

    def _rotate_left(self, x):
        """Auxiliary function to rotate left"""
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        """Auxiliary function to rotate right"""
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _splay(self, x):
        """Auxiliary function to splay the tree"""
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self._rotate_right(x.parent)
                else:
                    self._rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._rotate_right(x.parent.parent)
                self._rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._rotate_left(x.parent.parent)
                self._rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self._rotate_left(x.parent)
                self._rotate_right(x.parent)
            else:
                self._rotate_right(x.parent)
                self._rotate_left(x.parent)

    def insert_without_splay(self, key):
        """Function to insert a value like a binary tree"""
        if not self._root:
            self._root = Node(key)
            self._nodes += 1
            return

        node = self._root
        while node:
            if key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(key)
                    self._nodes += 1
                    node.left.parent = node
                    node = node.left
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(key)
                    self._nodes += 1
                    node.right.parent = node
                    node = node.right
            else:
                return

    def insert_with_splay(self, key):
        """Function to insert a value and splay it"""
        if not self._root:
            self._root = Node(key)
            self._nodes += 1
            return

        node = self._root
        while node:
            if key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(key)
                    self._nodes += 1
                    node.left.parent = node
                    node = node.left
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(key)
                    self._nodes += 1
                    node.right.parent = node
                    node = node.right
            else:
                # If the key is already in the tree, splay the node and return
                self._splay(node)
                return

        # Splay the newly-inserted node
        self._splay(node)

    def search(self, key):
        """Returns the node if exists and splay the tree"""
        node = self._root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                self._splay(node)
                return node
        return None

    def min(self, node=None):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        while pointer.left:
            pointer = pointer.left
        print(pointer.key)

    def max(self, node=None):
        """Returns the lowest value in the tree or subtree"""
        if node is None:
            pointer = self._root
            if self._root is None:
                raise Exception("The tree is empty")
        while pointer.right:
            pointer = pointer.right
        print(pointer.key)

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
            if left_height > right_height:
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
        """Prints the Tree"""
        if node is None:
            node = self._root
        lines, *_ = self._printTree(node)
        for line in lines:
            print(line)

    def _printTree(self, node):
        """Auxiliary function to print the Tree"""
        if node.right is None and node.left is None:  # No child
            line = "%s" % node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:  # Only left child
            lines, n, p, x = self._printTree(node.left)
            s = "%s" % node.key
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left is None:  # Only right child
            lines, n, p, x = self._printTree(node.right)
            s = "%s" % node.key
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._printTree(node.left)  # Two children
        right, m, q, y = self._printTree(node.right)
        s = "%s" % node.key
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    tree = SplayTree()
    tree.insert_without_splay(10)
    tree.insert_without_splay(4)
    tree.insert_without_splay(11)
    tree.insert_without_splay(12)
    tree.insert_without_splay(13)
    tree.insert_without_splay(2)
    tree.insert_without_splay(1)
    tree.insert_without_splay(3)
    tree.insert_without_splay(6)
    tree.insert_without_splay(5)
    tree.insert_without_splay(8)
    tree.insert_without_splay(7)
    tree.insert_without_splay(9)
    print("Original Tree:\n")
    tree.printTree()
    tree.search(3)
    print("\nAfter search 3:\n")
    tree.printTree()
    tree.search(9)
    print("\nAfter search 9:\n")
    tree.printTree()
    tree.search(1)
    print("\nAfter search 1:\n")
    tree.printTree()
    tree.search(5)
    print("\nAfter search 5:\n")
    tree.printTree()
