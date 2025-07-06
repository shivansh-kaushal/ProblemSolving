# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[root]]
        record = [[root.val]]

        while queue:
            next_level_nodes = []
            level_node_values = []
            
            for node in queue[0]:
                if node.left:
                    level_node_values.append(node.left.val)
                    next_level_nodes.append(node.left)
                if node.right:
                    level_node_values.append(node.right.val)
                    next_level_nodes.append(node.right)
            
            queue.pop(0)
            if next_level_nodes:
                record.append(level_node_values)
                queue.append(next_level_nodes)
        
        return record
