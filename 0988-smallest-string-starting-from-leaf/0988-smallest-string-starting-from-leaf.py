from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        self.answer = "~"

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.traverse(root, [])
        return self.answer

    def traverse(self, root: TreeNode, currPath: List[str]) -> None:
        if root == None:
            return

        currPath.append(self.getChar(root.val))
        if root.left == None and root.right == None:
            self.answer = min(self.answer, "".join(reversed(currPath)))
        self.traverse(root.left, currPath)
        self.traverse(root.right, currPath)
        currPath.pop()

    def getChar(self, num: int) -> str:
        return chr(num + ord('a'))