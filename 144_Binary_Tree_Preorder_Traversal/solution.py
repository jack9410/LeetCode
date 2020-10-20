# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        
        def _preorderTraversal(root):
            if root is None:
                pass
            else:
                answer.append(root.val)
                _preorderTraversal(root.left)
                _preorderTraversal(root.right)
        
        _preorderTraversal(root)
        return answer
                
        