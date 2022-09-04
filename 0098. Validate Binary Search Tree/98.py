from typing import Optional
from utils.tree import TreeNode, create_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checkSub(root, low, high):
            if low is not None and root.val <= low:
                return False
            if high is not None and root.val >= high:
                return False
            if root.left:
                if not checkSub(root.left, low, root.val):
                    return False

            if root.right:
                return checkSub(root.right, root.val, high)

            return True

            # return checkSub(root.left, low, root.val) and checkSub(root.right, root.val, high)

        if root.left and not checkSub(root.left, None, root.val):
            return False

        if root.right:
            return checkSub(root.right, root.val, None)

        return True

        # return checkSub(root.left, None, root.val) and checkSub(root.right, root.val, None)

    # online solution
    def isValidBST2(self, root, lessThan=float('inf'), largerThan=float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))

if __name__ == '__main__':
    solution = Solution()
    test = [0,None,-1]
    print(solution.isValidBST((create_tree((test)))))
