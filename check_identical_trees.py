# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, p,q):
        if p==None and q==None:
            return
        if p==None and q!= None:
            self.flag = False
            return
        if p!=None and q==None:
            self.flag = False
            return
        if p!=None and q!=None and p.val != q.val:
            self.flag = False
            return
        

        self.dfs(p.left, q.left)
        self.dfs(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        self.dfs(p, q)
        return self.flag