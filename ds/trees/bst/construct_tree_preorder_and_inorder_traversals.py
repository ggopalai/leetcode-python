# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        # preorder[1 : mid+1] - mid + 1 is determined by the position of the mid in inorder. as we know this position will give u the length of the left subtree, 
        # we can use it to determine how many values in the preorder list belongs to left subtree as well. 
        root.left = self.buildTree(preorder[1 : mid+1], inorder[ : mid]) 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1 : ])
        
        return root
        