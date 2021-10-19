### [20\. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Difficulty: **Easy**  

Related Topics: [String](https://leetcode.com/tag/string/), [Stack](https://leetcode.com/tag/stack/)


Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "()[]{}"
Output: true
```

**Example 3:**

```
Input: s = "(]"
Output: false
```

**Example 4:**

```
Input: s = "([)]"
Output: false
```

**Example 5:**

```
Input: s = "{[]}"
Output: true
```

**Constraints:**

*   `1 <= s.length <= 10<sup>4</sup>`
*   `s` consists of parentheses only `'()[]{}'`.


#### Solution

Language: **Python3**

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        buf = []
        pairs = {"(":")", "[":"]","{":"}"}
        for c in s:
            if c == '(' or c== "[" or c == "{":
                buf.append(c)
            else:
                if len(buf) == 0:
                    return False
                lastC = buf[-1]
                if c == pairs[lastC]:
                    buf.pop()
                else:
                    return False
                
        if len(buf) == 0:
            return True
```