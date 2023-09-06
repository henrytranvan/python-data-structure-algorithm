class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BinarySearchTrees:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if current_node.value == val:
                return False
            if current_node.value > val:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                else:
                    current_node = current_node.right


my_tree = BinarySearchTrees()
my_tree.insert(50)
my_tree.insert(40)
my_tree.insert(30)
my_tree.insert(60)
my_tree.insert(70)
my_tree.insert(80)

print(my_tree.root.right.right.value)
