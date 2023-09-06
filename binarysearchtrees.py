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

    def contain(self, val):
        current_node = self.root
        while current_node is not None:
            if current_node.value == val:
                return True
            elif current_node.value < val:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return False

    def __r_contain(self, current_node, val):
        if current_node is None:
            return False
        if current_node.value == val:
            return True
        if val < current_node.value:
            return self.__r_contain(current_node.left, val)
        else:
            return self.__r_contain(current_node.right, val)

    def r_contain(self, val):
        return self.__r_contain(self.root, val)

    def __r_insert(self, current_node, val):
        if current_node is None:
            return
        if current_node.value == val:
            return
        if val < current_node.value:
            if current_node.left is None:
                current_node.left = current_node
            else:
                self.__r_insert(current_node.left, val)
        else:
            if current_node.right is None:
                current_node.right = current_node
            else:
                self.__r_insert(current_node.right, val)

    def r_insert(self, val):
        return self.__r_insert(self.root, val)


my_tree = BinarySearchTrees()
my_tree.insert(50)
my_tree.insert(40)
my_tree.insert(30)
my_tree.insert(60)
my_tree.insert(70)
my_tree.insert(80)

print(my_tree.root.right.right.value)

if my_tree.contain(80):
    print("80 is in the tree")
else:
    print("80 is not in the tree")

if my_tree.contain(90):
    print("90 is in the tree")
else:
    print("90 is not in the tree")

if my_tree.r_contain(80):
    print("80 is in the tree")
else:
    print("80 is not in the tree")

if my_tree.r_contain(90):
    print("90 is in the tree")
else:
    print("90 is not in the tree")


my_tree = BinarySearchTrees()
my_tree.r_insert(55)
my_tree.insert(45)
my_tree.insert(35)
my_tree.insert(65)
my_tree.insert(75)
my_tree.insert(85)


if my_tree.r_contain(85):
    print("85 is in the tree")
else:
    print("85 is not in the tree")

if my_tree.r_contain(95):
    print("95 is in the tree")
else:
    print("95 is not in the tree")
