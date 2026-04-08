class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

        def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(f"{curr.data} ->", end=" ")
            curr = curr.next
        print("null")

    def search(self, target):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == target:
                return pos
            curr = curr.next
            pos += 1
        return -1