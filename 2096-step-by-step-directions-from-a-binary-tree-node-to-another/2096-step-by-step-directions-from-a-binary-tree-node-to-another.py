# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time:  O(n)
# Space: O(h)


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def dfs(node, val, path):
            if node.val == val:
                return True
            if node.left and dfs(node.left, val, path):
                path.append('L')
            elif node.right and dfs(node.right, val, path):
                path.append('R')
            return path

        src, dst = [], []
        dfs(root, startValue, src)
        dfs(root, destValue, dst)
        while len(src) and len(dst) and src[-1] == dst[-1]:
            src.pop()
            dst.pop()
        dst.reverse()
        return "".join(['U']*len(src) + dst)
        