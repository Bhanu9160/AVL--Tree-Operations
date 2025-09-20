class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Insertion
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Perform rotations if needed
        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Deletion
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance factor
        balance = self.get_balance(root)

        # Balancing the node
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Left Rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Right Rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Get height of node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Get node with minimum key
    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    # In-order Traversal
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.key, end=' ')
            self.in_order(root.right)

    # Pre-order Traversal
    def pre_order(self, root):
        if root:
            print(root.key, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    # Search
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

avl = AVLTree()
root = None

# Insert keys
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

print("In-order traversal after insertions:")
avl.in_order(root)  # Output: 10 20 25 30 40 50
print("\n")

# Pre-order (shows structure)
print("Pre-order traversal (tree structure):")
avl.pre_order(root)
print("\n")

# Delete a node
key_to_delete = 30
print(f"Deleting key {key_to_delete}")
root = avl.delete(root, key_to_delete)

print("In-order traversal after deletion:")
avl.in_order(root)
print("\n")

# Search for a key
search_key = 25
found_node = avl.search(root, search_key)
if found_node:
    print(f"Key {search_key} found in the tree.")
else:
    print(f"Key {search_key} not found in the tree.")
