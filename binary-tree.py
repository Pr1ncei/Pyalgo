class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def display_tree(self, node):
        if node:
            self.display_tree(node.left)
            print(node.value, end=" ")
            self.display_tree(node.right)

    def insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)

        return node

    def search(self, node, value):
        if node is None or node.value == value:
            return node

        if node.value < value:
            return self.search(node.right, value)

        return self.search(root.left, value)

    def get_maximum_value_node(self, node):
            current = node
            while current.right is not None:
                current = current.right

            return current

    def get_minimum_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def sum_of_all_elements(self, node):
        if node is None:
            return 0

        return node.value + self.sum_of_all_elements(node.left) + self.sum_of_all_elements(node.right)

    def minValueNode(self, node):
        current = node
        while curretn and current.left is not None:
            current = current.left

        return current

    def delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return node
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = minValueNode(node.right)
            node.value = temp.value
            node.right = delete(node.right, temp.value)

        return node