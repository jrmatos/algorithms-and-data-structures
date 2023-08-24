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
            return
            
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

        

    def print_in_order(self):
        self._print_in_order_node(self.root)

    def print_pre_order(self):
        self._print_pre_order(self.root)

    def print_post_order(self):
        self._print_post_order(self.root)

    def _print_in_order_node(self, node: Node):
        if node is None:
            return  # recursion base case (stop)

        self._print_in_order_node(node.left)
        print(str(node.key) + "(" + str(node.count) + ")")
        self._print_in_order_node(node.right)

    def _print_pre_order(self, node: Node):
        if node is None:
            return  # recursion base case (stop)

        print(str(node.key) + "(" + str(node.count) + ")")
        self._print_pre_order(node.left)
        self._print_pre_order(node.right)

    def _print_post_order(self, node: Node):
        if node is None:
            return  # recursion base case (stop)

        self._print_post_order(node.left)
        self._print_post_order(node.right)
        print(str(node.key) + "(" + str(node.count) + ")")


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

    tree.print_in_order()
    print("------")
    tree.print_pre_order()
    print("------")
    tree.print_post_order()
