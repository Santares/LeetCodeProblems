### [4\. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Difficulty: **Hard**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Binary Search](https://leetcode.com/tag/binary-search/), [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/)


Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

**Constraints:**

*   `nums1.length == m`
*   `nums2.length == n`
*   `0 <= m <= 1000`
*   `0 <= n <= 1000`
*   `1 <= m + n <= 2000`
*   `-10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup>`


#### Solution

Language: **Python3**

```python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        m = (l1 + l2) /2
        res = 0
            
        j = 0
        k = 0
        while i < m :
            if j >= l1:
                res = nums2[k]
                k+=1
            elif k >= l2:
                res = nums1[j]
                j+=1
            elif nums1[j] <= nums2[k]:
                res = nums1[j]
                j += 1
            else:
                res = nums2[k]
                k += 1
            i += 1
        
        if (l1 + l2) % 2 == 0:
            if j >= l1:
                res = (res + nums2[k]) / 2
                k+=1
            elif k >= l2:
                res = (res + nums1[j]) / 2
            else:
                res = (res + min(nums1[j], nums2[k])) / 2
        else:
            if j >= l1:
                res = nums2[k]
                k+=1
            elif k >= l2:
                res = nums1[j]
            else:
                res = min(nums1[j], nums2[k])
        
        return res
        
        
```