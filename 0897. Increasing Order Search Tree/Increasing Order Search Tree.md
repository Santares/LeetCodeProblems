### [897\. Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)

Difficulty: **Easy**  

Related Topics: [Stack](https://leetcode.com/tag/stack/), [Tree](https://leetcode.com/tag/tree/), [Depth-First Search](https://leetcode.com/tag/depth-first-search/), [Binary Search Tree](https://leetcode.com/tag/binary-search-tree/), [Binary Tree](https://leetcode.com/tag/binary-tree/)


Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)

```
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)

```
Input: root = [5,1,7]
Output: [1,null,5,null,7]
```

**Constraints:**

*   The number of nodes in the given tree will be in the range `[1, 100]`.
*   `0 <= Node.val <= 1000`


#### Solution

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            lst.append(root.val)
            helper(root.right)

        helper(root)
        new_root = TreeNode(lst[0])
        cur = new_root
        for i in range(1, len(lst)):
            cur.right = TreeNode(lst[i])
            cur = cur.right
        return new_root

```