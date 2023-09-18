# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def toArray(root, nums):
            if not root:
                return

            toArray(root.left, nums)
            nums.append(root.val)
            toArray(root.right, nums)
            return

        nums1 = []
        nums2 = []
        toArray(root1, nums1)
        toArray(root2, nums2)
        left, right = 0, 0
        res = []
        while left < len(nums1) or right < len(nums2):
            if left < len(nums1) and right >= len(nums2):
                res += nums1[left:]
                break

            if left >= len(nums1) and right < len(nums2):
                res += nums2[right:]
                break

            if nums1[left] <= nums2[right]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1

        return res
