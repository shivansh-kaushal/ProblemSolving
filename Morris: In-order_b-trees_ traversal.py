# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        li = []

        curr = root
        while(curr):
            prev = curr.left
            if(prev):
                while prev.right != None and prev.right != curr:
                    prev = prev.right

                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    li.append(curr.val)
                    curr = curr.right
            else:
                li.append(curr.val)
                curr = curr.right

        return li
            
