# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass



class Solution(object):
    def evaluateTree(self, root):
        
        INF = float("inf")
        OP = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y,
        }
        
        def dfs(node):
            if node.left == node.right:
                return node.val
            return OP[node.val](dfs(node.left), dfs(node.right))

        return dfs(root)