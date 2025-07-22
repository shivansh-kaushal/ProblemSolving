# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find_max(self, node, maxi):
            if not node:
                return maxi
            
            lh = self.find_max(node.left, maxi)
            rh = self.find_max(node.right, maxi)

            self.max_diameter = max(self.max_diameter, lh + rh)
            return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.find_max(root, 0)
        
        return self.max_diameter
