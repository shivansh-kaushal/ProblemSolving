from typing import List

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    if not root:
        return []
    queue = [[root, 0]]
    dicty = {0: root.data}
    
    while queue:
        # getting first values, vertical line number from queue
        node = queue[0][0]
        tracker = queue[0][1]

        # left traversal
        if node.left:
            dicty[tracker -1] = node.left.data
            queue.append([node.left, tracker -1])

        # right traversal
        if node.right:
            dicty[tracker +1] = node.right.data
            queue.append([node.right, tracker + 1])

        queue.pop(0)

    bottom_view = []
    for key in sorted(dicty.keys()):
        bottom_view.append(dicty[key])

    return bottom_view
