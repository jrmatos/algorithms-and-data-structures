class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.count: int = 1
        self.left: Node = None
        self.right: Node = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_node(self.root, key)

    def _insert_node(self, node: Node, key: int):
        if node is None:
            node = Node(key)
            return # recursion base case (stop)
            
        elif key < node.key:
            if node.left is not None:
                self._insert_node(node.left, key)
            else:
                node.left = Node(key)

        elif key > node.key:
            if node.right is not None:
                self._insert_node(node.right, key)
            else:
                node.right = Node(key)

        else:
            node.count += 1  # equal/duplicated... then increment count

    def in_order_traverse(self, callback: callable):
        self._in_order_traverse_node(self.root, callback)

    def pre_order_traverse(self, callback: callable):
        self._pre_order_traverse(self.root, callback)

    def post_order_traverse(self, callback: callable):
        self._post_order_traverse(self.root, callback)

    def _in_order_traverse_node(self, node: Node, callback: callable):
        if node is None:
            return  # recursion base case (stop)

        self._in_order_traverse_node(node.left, callback)
        callback(node)
        self._in_order_traverse_node(node.right, callback)

    def _pre_order_traverse(self, node: Node, callback: callable):
        if node is None:
            return  # recursion base case (stop)

        callback(node)
        self._pre_order_traverse(node.left, callback)
        self._pre_order_traverse(node.right, callback)

    def _post_order_traverse(self, node: Node, callback: callable):
        if node is None:
            return  # recursion base case (stop)

        self._post_order_traverse(node.left, callback)
        self._post_order_traverse(node.right, callback)
        callback(node)

if __name__ == "__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)
    tree.insert(9)
    tree.insert(7)
    tree.insert(10)

    print("in order")
    tree.in_order_traverse(lambda node: print(str(node.key) + "(" + str(node.count) + ")"))
    print("pre order")
    tree.pre_order_traverse(lambda node: print(str(node.key) + "(" + str(node.count) + ")"))
    print("post order")
    tree.post_order_traverse(lambda node: print(str(node.key) + "(" + str(node.count) + ")"))
