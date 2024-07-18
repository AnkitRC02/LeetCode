# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time:  O(n)
# Space: O(h)

import collections


class Solution(object):
    def countPairs(self, root, distance):
        def dfs(distance, node):
            if not node:
                return 0, collections.Counter()
            if not node.left and not node.right:
                return 0, collections.Counter([0])
            left, right = dfs(distance, node.left), dfs(distance, node.right)
            result = left[0]+right[0]
            for left_d, left_c in left[1].iteritems():
                for right_d,right_c in right[1].iteritems():
                    if left_d+right_d+2 <= distance:
                        result += left_c*right_c
            return result, collections.Counter({k+1:v for k,v in (left[1]+right[1]).iteritems()})
        
        return dfs(distance, root)[0]
        