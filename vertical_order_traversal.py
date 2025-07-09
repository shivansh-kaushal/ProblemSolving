# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return  []
        queue = [{0:[root]}]
        record = {0: [root.val]}

        while queue:
            next_level_nodes = {}
            level_val = {}
            for tracker in queue[0]:
                for node in queue[0][tracker]:
                    if  node.left:
                        if level_val.get(tracker - 1):
                            level_val[tracker -1].append(node.left.val)
                        else:
                            level_val[tracker -1] = [node.left.val]
                        if next_level_nodes.get(tracker -1):
                            next_level_nodes[tracker - 1].append(node.left)
                        else:
                            next_level_nodes[tracker - 1] = [node.left]

                    
                    if  node.right:
                        if level_val.get(tracker + 1):
                            level_val[tracker + 1].append(node.right.val)
                        else:
                            level_val[tracker + 1] = [node.right.val]
                        if next_level_nodes.get(tracker +1):
                            next_level_nodes[tracker + 1].append(node.right)
                        else:
                            next_level_nodes[tracker + 1] = [node.right]
                
            for tracker in level_val:
                if record.get(tracker):
                    record[tracker].extend(sorted(level_val[tracker]))
                else:
                    record[tracker] = sorted(level_val[tracker])
                 
            queue.pop(0)
            if next_level_nodes:
                queue.append(next_level_nodes)
        vertical_travel = [record[key] for key in sorted(record.keys())]
        return vertical_travel
            
