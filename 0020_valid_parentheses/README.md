# 0020. Valid Parentheses

## Problem

Given a string `s` containing only `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, check if the string is **valid**.

A string is valid if:

1. Every open bracket has a matching close.
2. Brackets close in the correct order.

**Examples**

```
Input: s = "()"
Output: true  

Input: s = "()[]{}"
Output: true  

Input: s = "(]"
Output: false  

Input: s = "([])"
Output: true
```

## Solutions

### Approach 1: Stack (Best Solution)

* Use a stack to store opening brackets.
* When we see a closing bracket, check if it matches the most recent opening bracket.
* At the end, if the stack is empty → valid string.
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

```python
class Solution(object):
    def isValid(self, s):
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
```


### Approach 2: Iterative Replacement (Simpler, but Slower)

* Keep removing `"()"`, `"[]"`, `"{}"` until no more pairs exist.
* If the string ends up empty → valid.
* **Time Complexity:** O(n²) (worst case, since we repeatedly scan).
* **Space Complexity:** O(1)

```python
class Solution(object):
    def isValid(self, s):
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == ""
```


### Why Stack Is Better

* Stack guarantees a clean **O(n)** solution.
* Replacement is more intuitive but gets inefficient for large strings.


### Key Takeaways

* Practiced applying stacks for parsing problems.
* Saw the tradeoff between a neat O(n) solution vs. a simple but slower approach.
* Learned to reason about correctness by manually walking through examples.
