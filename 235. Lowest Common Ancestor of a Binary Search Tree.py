# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if p.val > q.val:
      return self.lowestCommonAncestor(root, q, p)
    while root.val < p.val or root.val > q.val:
      if root.val < p.val:
        root = root.right
      else:
        root = root.left
    return root