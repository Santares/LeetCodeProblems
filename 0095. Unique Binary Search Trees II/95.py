# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Online solution
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right:
                return [None]

            res = []
            for i in range(left, right+1):
                leftRes = helper(left, i-1)
                rightRes = helper(i+1, right)
                for leftTree in leftRes:
                    for rightTree in rightRes:
                        head = TreeNode(i, leftTree, rightTree)
                        res.append(head)
            return res

        return helper(1, n)

if __name__ == '__main__':
    s = Solution()
    test = 3
    print(s.generateTrees(test))