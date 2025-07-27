# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        zigzag_trav = [[root.val]]
        count = 0
        while queue:
            next_level_nodes = []
            values = []

            for node in queue[0]:
                if node.left:
                    next_level_nodes.append(node.left)
                    values.append(node.left.val)
                if node.right:
                    next_level_nodes.append(node.right)
                    values.append(node.right.val)

            queue.pop(0)
            if next_level_nodes:
                if count%2 == 0:
                    values = values[::-1]
                zigzag_trav.append(values)
                queue.append(next_level_nodes)

            count += 1

        return zigzag_trav