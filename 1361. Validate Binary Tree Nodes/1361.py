from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = [False] * n
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            if left != -1:
                if hasParent[left] != False:
                    return False
                else:
                    hasParent[left] = True
            if right != -1:
                if hasParent[right] != False:
                    return False
                else:
                    hasParent[right] = True

        root = -1
        for i, x in enumerate(hasParent):
            if not x:
                if root != -1:
                    return False
                else:
                    root = i

        def helper(root):
            if root == -1:
                return 0
            else:
                return helper(leftChild[root]) + 1 + helper(rightChild[root])

        if helper(root) != n:
            return False

        return True


if __name__ == '__main__':
    s = Solution()
    test1 = 4
    test2 = [1,-1,3,-1]
    test3 = [2,-1,-1,-1]
    # test1 = 4
    # test2 = [1,0,3,-1]
    # test3 = [-1,-1,-1,-1]
    print(s.validateBinaryTreeNodes(test1, test2, test3))