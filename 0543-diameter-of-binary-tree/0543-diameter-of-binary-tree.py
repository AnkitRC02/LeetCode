class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxx =0;
        
        def levels(root):
            if not root: return 0;
            left, right = levels(root.left), levels(root.right)
            self.maxx = max(self.maxx, left+right)
            return 1 + max(left, right)
                # return 0;
        levels(root)
        return self.maxx        