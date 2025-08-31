# 0020. Valid Parentheses

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every closing bracket must have a corresponding opening bracket.

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

**Constraints**

* 1 <= s.length <= 10⁴
* s consists only of `'()[]{}'`

---

## Solutions

### Approach 1: Stack (Best Solution)

* Use a stack to track opening brackets.
* When a closing bracket is found, check if it matches the last opening bracket.
* If not, return False.
* At the end, if the stack is empty, return True.

**Time Complexity**: O(n)
**Space Complexity**: O(n)

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

---

### Approach 2: Iterative Replacement (This One Is More Simpler Than the First)

* Repeatedly remove `"()"`, `"[]"`, and `"{}"` from the string.
* Continue until no more pairs can be removed.
* If the final string is empty, it was valid.

**Time Complexity**: O(n²) (worst case)
**Space Complexity**: O(1)

```python
class Solution(object):
    def isValid(self, s):
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == ""
```

---

### Why Stack Is Better?

* **Stack** guarantees O(n) processing, no repeated scanning.
* **Replacement** is intuitive but inefficient for long strings.

---

### What Did I Learn?

* Practiced using **stack data structures** for parsing problems.
* Understood difference between **efficient O(n)** vs. **naive O(n²)** approaches.
* Learned to check correctness by tracing examples step by step.
