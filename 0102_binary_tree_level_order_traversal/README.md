# 0102. Binary Tree Level Order Traversal

## Problem

Given the root of a binary tree, return the level order traversal of its nodes’ values — i.e., from left to right, level by level.

**Examples**

```
Input:  root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input:  root = [1]
Output: [[1]]

Input:  root = []
Output: []
```

**Constraints**

* The number of nodes is in the range `[0, 2000]`.
* `-1000 <= Node.val <= 1000`

## Solutions

### Approach 1: Breadth-First Search (Optimal)

* Use a queue to traverse the tree level by level.
* For each level, process all nodes currently in the queue, add their children for the next level.
* **Time Complexity:** O(n) — each node visited once
* **Space Complexity:** O(n) — queue stores at most one level

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        q = deque([root])

        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans
```

### Approach 2: Brute Force (Naive Depth Scan per Level)

* First find the height of the tree.
* For each depth `d` from 0 to height-1, scan the tree recursively and collect all nodes at that depth.
* Very inefficient: each level requires re-scanning much of the tree.
* **Time Complexity:** O(n·h) in worst case (skewed tree → O(n²))
* **Space Complexity:** O(h) recursion depth

```python
# class TreeNode(object): ...

class Solution(object):
    def levelOrder(self, root):
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def collectLevel(node, level, res):
            if not node:
                return
            if level == 0:
                res.append(node.val)
            else:
                collectLevel(node.left, level - 1, res)
                collectLevel(node.right, level - 1, res)

        h = height(root)
        ans = []
        for d in range(h):
            level_nodes = []
            collectLevel(root, d, level_nodes)
            ans.append(level_nodes)
        return ans
```

### Key Takeaways

* **BFS with a queue** is the natural and optimal way for level order traversal.
* The **brute force depth scan** works but repeats a lot of work → mainly useful for understanding recursion, not for real use.
