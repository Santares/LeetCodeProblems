# import sys
# sys.path.append("..")
# import utils.tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(nums: List[int]) -> Optional[TreeNode]:
    numLen = len(nums)
    if numLen == 0:
        return None
    root = TreeNode(nums[0])
    stack = [root]

    tmp = []
    i = 1
    while i < numLen:
        for node in stack:
            if i >= numLen:
                break
            if nums[i] is not None:
                node.left = TreeNode(nums[i])
                tmp.append(node.left)
            if i+1 < numLen and nums[i+1] is not None:
                node.right = TreeNode(nums[i+1])
                tmp.append(node.right)
            i += 2
        stack = tmp[:]
        tmp.clear()

    return root


# test = [2,1,3]
# test = [5,1,4,None,None,3,6]
# test = [2,2,2]
# test = [0,None,-1]
# root = create_tree(test)
# print(root)


