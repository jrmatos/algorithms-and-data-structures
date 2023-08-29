class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.count: int = 1
        self.left: Node = None
        self.right: Node = None

class BST:
    def __init__(self):
        self.root = None

    def _is_empty(self):
        return self.root is None

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

    def get_min(self):
        if self._is_empty():
            raise Exception("Tree is empty")
        
        return self._get_min_node(self.root)

    def _get_min_node(self, node: Node):
        if node.left is not None:
            return self._get_min_node(node.left)

        return node.key

    def get_max(self):
        if self._is_empty():
            raise Exception("Tree is empty")
        
        return self._get_max_node(self.root)
    
    def _get_max_node(self, node: Node):
        if node.right is not None:
            return self._get_max_node(node.right)

        return node.key

    # return how many occurrences of key there is in tree
    def find(self, key: int) -> int:
        return self._find_node(key, self.root)

    def _find_node(self, key: int, node: Node):
        if node is None:
            return 0
        
        if node.key == key:
            return node.count
        
        if key < node.key:
            return self._find_node(key, node.left)

        if key > node.key:
            return self._find_node(key, node.right)
    
    def delete_all(self):
        self._in_order_traverse_node(self.root, self._delete_node_children)
        self.root = None

    def _delete_node_children(self, node: Node):
        node.left = None
        node.right = None

    def delete(self, key: int) -> bool:
        if self._delete_node_by_key(self.root, key) is not None:
            return True
        return False

    def _delete_node_by_key(self, node: Node, key: int) -> Node:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_node_by_key(node.left, key)
        elif key > node.key:
            node.right = self._delete_node_by_key(node.right, key)
        else:
            if node.count > 1:
                node.count -= 1
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children
                min_right = self._get_min_node(node.right)
                node.key = min_right
                node.count -= 1
                node.right = self._delete_node_by_key(node.right, min_right)

        return node
    
    def print_node(self, node: Node):
        occurrences = ("(" + str(node.count) + ")" if node.count > 1 else "")
        print(str(node.key) + occurrences)

if __name__ == "__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(4)
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(35)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)
    tree.insert(8)
    tree.insert(8)
    tree.insert(9)
    tree.insert(7)
    tree.insert(10)

    # assert tree.find(9) == 1
    # assert tree.find(7) == 2
    # assert tree.find(8) == 3
    # assert tree.get_min() == 1
    # assert tree.get_max() == 35

    print("in order")
    tree.in_order_traverse(tree.print_node)
    print("pre order")
    tree.pre_order_traverse(tree.print_node)
    print("post order")
    tree.post_order_traverse(tree.print_node)

    tree.delete(8)
    tree.delete(8)
    tree.delete(8)
    tree.delete(35)
    # tree.delete_all()

    print("in order")
    tree.in_order_traverse(tree.print_node)

