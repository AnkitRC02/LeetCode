# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def delNodes(self, root, to_delete):
        def delNodesHelper(to_delete_set, root, is_root, result):
            if not root:
                return None
            is_deleted = root.val in to_delete_set
            if is_root and not is_deleted:
                result.append(root)
            root.left = delNodesHelper(to_delete_set, root.left, is_deleted, result)
            root.right = delNodesHelper(to_delete_set, root.right, is_deleted, result)
            return None if is_deleted else root
        
        result = []
        to_delete_set = set(to_delete)
        delNodesHelper(to_delete_set, root, True, result)
        return result
        