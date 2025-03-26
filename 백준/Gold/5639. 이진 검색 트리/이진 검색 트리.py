import sys
sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst(preorder, start, end):
    if start > end:
        return None, start
    
    root_value = preorder[start]
    root = Node(root_value)
    index = start + 1

    while index <= end and preorder[index] < root_value:
        index += 1

    root.left, index = build_bst(preorder, start + 1, index -1)
    root.right, index = build_bst(preorder, index, end)

    return root, index

def build_postorder(node):
    if node is None:
        return []
    return build_postorder(node.left) + build_postorder(node.right) + [node.value]


preorder = list(map(int, sys.stdin.read().splitlines()))

root, _ = build_bst(preorder, 0, len(preorder) - 1)
postorder = build_postorder(root)

print('\n'.join(map(str, postorder)))
