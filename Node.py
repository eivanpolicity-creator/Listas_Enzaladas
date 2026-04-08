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

        def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_by_value(self, value):
        if not self.head: return
        if self.head.data == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def get_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

        def sort_by_links(self):
        if not self.head or not self.head.next:
            return
        
        changed = True
        while changed:
            changed = False
            prev = None
            curr = self.head
            while curr and curr.next:
                if curr.data > curr.next.data:
                    
                    temp = curr.next
                    curr.next = temp.next
                    temp.next = curr
                    
                    if prev is None:
                        self.head = temp
                    else:
                        prev.next = temp
                    
                    changed = True
                    prev = temp 
                else:
                    prev = curr
                    curr = curr.next


