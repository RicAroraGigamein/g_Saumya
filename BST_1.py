class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif key > root.val:
        root.right = deleteNode(root.right, key)

    else:
        # Case 1: No child
        if not root.left and not root.right:
            return None

        # Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Two children
        # Find inorder successor (smallest in right subtree)
        successor = findMin(root.right)
        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)

    return root


def findMin(node):
    while node.left:
        node = node.left
    return node


# Helper for inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Example
root = None

# Build BST
values = [5,3,6,2,4,7]
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

for v in values:
    root = insert(root, v)

# Delete node
root = deleteNode(root, 3)

inorder(root)


# deletion and inseertion
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif key > root.val:
        root.right = deleteNode(root.right, key)

    else:
        # Case 1: No child
        if not root.left and not root.right:
            return None

        # Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Two children
        # Find inorder successor (smallest in right subtree)
        successor = findMin(root.right)
        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)

    return root


def findMin(node):
    while node.left:
        node = node.left
    return node


# Helper for inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Example
root = None

# Build BST
values = [5,3,6,2,4,7]
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

for v in values:
    root = insert(root, v)

# Delete node
root = deleteNode(root, 3)

inorder(root)