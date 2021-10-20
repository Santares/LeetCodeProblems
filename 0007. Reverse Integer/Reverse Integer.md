### [7\. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Difficulty: **Medium**  

Related Topics: [Math](https://leetcode.com/tag/math/)


Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2<sup>31</sup>, 2<sup>31</sup> - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

```
Input: x = 123
Output: 321
```

**Example 2:**

```
Input: x = -123
Output: -321
```

**Example 3:**

```
Input: x = 120
Output: 21
```

**Example 4:**

```
Input: x = 0
Output: 0
```

**Constraints:**

*   `-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1`


#### Solution

Language: **Python3**

```python3
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 -1 or x < -1 * 2**31:
            return 0
        s = str(x)
        if x < 0:
            s = s[:0:-1]
        else:
            s = s[::-1]
        y = int(s)
        if x < 0:
            y = y * -1
        
        return y
        
```