# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [[root]]
        record = []
        while(queue):
            next_level_nodes = []
            fucking_data = []
            for node in queue[0]:
                if(node.left):
                    next_level_nodes.append(node.left)
                if(node.right):
                    next_level_nodes.append(node.right)
            record.append(node.val)

            queue.pop(0)
            if(next_level_nodes):
                queue.append(next_level_nodes)
        
        return record
                
