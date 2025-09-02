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