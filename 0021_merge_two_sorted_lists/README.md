# 0021. Merge Two Sorted Lists

## Problem

You’re given the heads of two **sorted linked lists** (`list1` and `list2`).
The goal is to merge them into one sorted linked list by splicing the nodes together — then return the head of the merged list.

**Examples**

```
Input:  list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]  

Input:  list1 = [], list2 = []  
Output: []  

Input:  list1 = [], list2 = [0]  
Output: [0]
```

**Constraints**

* Number of nodes in both lists: `[0, 50]`
* `-100 <= Node.val <= 100`
* Both lists are sorted in **non-decreasing order**

## Solutions

### Approach 1: Iterative with Dummy Node

* Create a **dummy node** to simplify edge cases.
* Use a pointer (`tail`) to build the merged list.
* Compare `list1.val` and `list2.val` at each step, attach the smaller one, and move forward.
* Once one list ends, just attach the rest of the other list.
* **Time Complexity:** O(m+n)
* **Space Complexity:** O(1) (in-place merge)

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remainder
        tail.next = list1 if list1 else list2
        return dummy.next
```

### Approach 2: Recursive Solution (Elegant, but Stack-Heavy)

* Base case: if one list is empty → return the other.
* Otherwise, pick the smaller head and recursively merge the rest.
* **Time Complexity:** O(m+n)
* **Space Complexity:** O(m+n) (due to recursion stack)

```python
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

### Approach 3: Convert to Python List and Back (Not Optimal)

* Traverse both lists, collect all values in a Python list.
* Sort it, then rebuild the linked list.
* Works fine for small inputs but inefficient.
* **Time Complexity:** O((m+n) log(m+n))
* **Space Complexity:** O(m+n)

```python
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        values = []
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        values.sort()

        dummy = ListNode()
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next
```

### Why Iterative with Dummy Node Is Best

* Recursive is clean but limited by Python’s recursion depth.
* Converting to lists is easy but wastes memory and time.
* Iterative dummy node method is **efficient, clean, and handles all cases in O(m+n)**.

### Key Takeaways

* Learned how **dummy nodes** simplify linked list operations.
* Understood the tradeoff between **recursion elegance vs. iteration efficiency**.
* Saw the difference between in-place merging and rebuilding from scratch.
