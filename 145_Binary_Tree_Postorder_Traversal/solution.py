# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        
        def _postorderTraversal(root):
            if root is None:
                pass
            else:
                _postorderTraversal(root.left)
                _postorderTraversal(root.right)
                answer.append(root.val)
        
        _postorderTraversal(root)
        
        return answer
        