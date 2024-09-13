class Node:
    
    def __init__(self, data):
        self._data = data
        self.children = []

    def insert(self, node: 'Node'):
        self.children.append(node)

    def printTree(self):
        print()

    def print_tree(self, level=0):
        indent = ' ' * (level * 4)  # Indentation increases with depth
        print(f"{indent}{self._data}")
        for child in self.children:
            child.print_tree(level + 1)

# Example usage:
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
child3 = Node("Child 3")
grandchild1 = Node("Grandchild 1")
grandchild2 = Node("Grandchild 2")

# Build the tree structure
root.insert(child1)
root.insert(child2)
child1.insert(grandchild1)
child1.insert(grandchild2)
root.insert(child3)

# Print the tree structure
root.print_tree()