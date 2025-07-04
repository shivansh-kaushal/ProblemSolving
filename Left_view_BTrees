from os import *
from sys import *
from collections import *
from math import *
from builtins import open

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeftView(root)->list:
    # Write your code here
    # Return a list
    if(root == None):
        return []

    queue = [[root]]
    record = []

    while(queue):
        level_node = queue[0]
        next_level = []
        next_level_nodes = []
        for node in level_node:
            if(node.left):
                next_level_nodes.append(node.left)

            if(node.right):
                next_level_nodes.append(node.right)
            
            next_level.append(node.data) 
        record.append(next_level[0])
        queue.pop(0)    
        if(next_level_nodes):
            queue.append(next_level_nodes)

    return record
            

















