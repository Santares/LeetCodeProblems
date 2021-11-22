# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # not acceptable
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        roots = []
        end = False
        leaf = inorder.pop()

        while postorder:
            num = postorder.pop()
            if inorder and end:
                leaf = inorder.pop()

            if not end and num != leaf:
                roots.append(TreeNode(num))
            elif end and num != leaf:
                last = roots.pop()
                if roots:
                    roots[-1].right = last
                else:
                    roots.append(last)
                if num == leaf:
                    roots[-1].left = TreeNode(num)
                else:
                    postorder.append(num)
            elif not end and num == leaf:
                end = True
                if not roots:
                    roots.append(TreeNode(leaf))
                    continue
                last = roots[-1]
                last.right = TreeNode(leaf)
                # if leaf == last:
                if not inorder:
                    return last
                leaf = inorder.pop()
            else:
                last = roots.pop()
                if roots:
                    last.left = TreeNode(leaf)
                    roots[-1].right = last
                else:
                    head = last
                    while last.left:
                        last = last.left
                    last.left = TreeNode(leaf)
                    roots.append(head)
                    # return last

        return roots[-1]

    # based on online solution
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i, x in enumerate(inorder):
            dic[x] = i
        l = len(inorder)

        def build(inStart, inEnd, postStart, postEnd):
            root = TreeNode(postorder[postEnd])
            if inEnd == inStart:
                return root
            elif inEnd < inStart:
                return None

            rootIndex = dic[postorder[postEnd]]
            rightLen = inEnd - rootIndex
            root.left = build(inStart, rootIndex-1, postStart, postEnd - rightLen - 1)
            root.right = build(rootIndex + 1, inEnd, postEnd - rightLen, postEnd - 1)

            return root

        return build(0, l-1, 0, l-1)

    # online solution
    def buildTree3(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)








if __name__ == '__main__':
    solution = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    # inorder = [9, 3, 20, 7, 15]
    # postorder = [9, 15, 7, 20, 3]
    # inorder = [2,1]
    # postorder = [2,1]
    # inorder = [1]
    # postorder = [1]
    # inorder = [3, 2, 1]
    # postorder = [3,2,1]
    tree = solution.buildTree2(inorder, postorder)
    print(TreeNode)