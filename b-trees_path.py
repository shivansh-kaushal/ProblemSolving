# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue = [{root: str(root.val)}]
        final_paths = []

        while queue:
            next_level_nodes = {}
            for node in queue[0]:
                if node.left:
                    next_level_nodes[node.left] = queue[0][node] + '->' + str(node.left.val) 
                if node.right:
                    next_level_nodes[node.right] = queue[0][node] + '->' + str(node.right.val) 
                if not node.left and not node.right:
                    final_paths.append(queue[0][node])
            
            
            if next_level_nodes:
                queue.append(next_level_nodes)
            
            queue.pop(0)

        return final_paths
