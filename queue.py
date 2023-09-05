class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def append(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def delete(self):
        self.head = self.head.next
        self.length -= 1

    def pop_out(self):
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        self.tail = current_node
        self.tail.next = None
        self.length -= 1

    def insert(self, pos_val, val):
        new_node = Node(val)
        current_node = self.head
        while current_node != None and current_node.value != pos_val:
            current_node = current_node.next
        if current_node == self.tail:
            self.append(val)
        else:
            new_node.next = current_node.next
            current_node.next = new_node

        self.length += 1

    def print_ll(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next



my_ll = LinkedList(20)
my_ll.append(50)
my_ll.append(40)

my_ll.print_ll()
print("=======================")

my_ll.prepend(90)
print(my_ll.head.value)
print(my_ll.head.next.value)
print(my_ll.tail.value)
print(my_ll.tail.next)
print(my_ll.length)
print("+++++++++++++++++++")

my_ll.print_ll()

print("=======================")

my_ll.insert(90, 80)
print(my_ll.head.value)
print(my_ll.head.next.value)
print(my_ll.tail.value)
print(my_ll.tail.next)
print(my_ll.length)

print("+++++++++++++++++++")

my_ll.print_ll()

print("=======================")