# Problems

| Problem Number | Problem Name                                               | Difficulty | Link                                                         | Notes            |
| -------------- | ---------------------------------------------------------- | ---------- | ------------------------------------------------------------ | ---------------- |
| 5              | Longest Palindromic Substring                              | Medium     | https://leetcode.com/problems/longest-palindromic-substring/ |                  |
| 127            | Word Ladder                                                | Hard       | https://leetcode.com/problems/word-ladder/                   | Time Limit       |
| 96             | Unique Binary Search Trees                                 | Medium     | https://leetcode.com/problems/unique-binary-search-trees/    |                  |
| 121            | Best Time to Buy and Sell Stock                            | Easy       | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |                  |
| 10             | Regular Expression Matching                                | Hard       | https://leetcode.com/problems/regular-expression-matching/   |                  |
| 739            | Daily Temperatures                                         | Medium     | https://leetcode.com/problems/daily-temperatures/            | Time Limit       |
| 11             | Container With Most Water                                  | Medium     | https://leetcode.com/problems/container-with-most-water/     | Wrong            |
| 368            | Largest Divisible Subset                                   | Medium     | https://leetcode.com/problems/largest-divisible-subset/      | Time Limit       |
| 41             | First Missing Positive                                     | Hard       | https://leetcode.com/problems/first-missing-positive/        | Not O(n)         |
| 407            | Trapping Rain Water II                                     | Hard       | https://leetcode.com/problems/trapping-rain-water-ii/        | Time Limit       |
| 84             | Largest Rectangle in Histogram                             | Hard       | https://leetcode.com/problems/largest-rectangle-in-histogram/ | Time Limit       |
| 106            | Construct Binary Tree from Inorder and Postorder Traversal | Medium     | https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/ | Wrong/Time Limit |



#### 127







#### 10







#### 739

use stack to find next/previous larger/smaller number

**Similar problems**: 

+ 496 https://leetcode.com/problems/next-greater-element-i/
  + use **hash map**
+ 901 https://leetcode.com/problems/online-stock-span/
  + use stack, **pop unneeded ones**
+ 503 https://leetcode.com/problems/next-greater-element-ii/
  +  double the length
+ 556 https://leetcode.com/problems/next-greater-element-iii/submissions



#### 11

think too much



**similar problems:**

* 42 https://leetcode.com/problems/trapping-rain-water/
  * from two side



#### 368







#### 41

not O(n) or space not O(1)

**sample solution:** 

- https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
- https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time



#### 407

Min heap + BFS

search from outer layer, using minimal one first

**sample solution:** 

* https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap





#### 84

O(n^2) to O(n)

use stack to store

**sample solution:** 

* https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)

```Python
    def largestRectangleArea5(self, heights: List[int]) -> int:
        heights.append(0) # important
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans
```





#### 106

Use the characteristic of inorder and postorder traverse

Use recursion to do left and right substree

**sample solution:** 

* https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/1588934/C%2B%2B-EASY-Intuitive-Sol-or-Clean-Recursive-Code-w-Explanation-(Dry-Run)-or-T.C%3AO(N)

**similar problems:**

* 105 https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
  * similar

