class Node:
    def __init__(self, val):
        self.next = None
        self.previous = None
        self.val = val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add(self, val):
        new_node = Node(val)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

        self.length += 1

    def remove(self, val):
        if self.head.val == val: # is head
            self.head = self.head.next
            self.length -= 1
            return

        if self.tail.val == val: # is tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return

        node = self.head.next

        while node:
            if node.val == val:
                node.previous.next = node.next
                
                self.length -= 1
                return

    def print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def is_empty(self):
        return self.head is None

    def get_length(self):
        return self.length


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.add(2)
    list.add(9)
    list.add(5)
    list.remove(2)
    list.print()
