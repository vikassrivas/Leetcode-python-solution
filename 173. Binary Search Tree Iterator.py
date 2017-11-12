# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = []
        cur = root
        while cur:
            self.path.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.path) > 0

    def next(self):
        """
        :rtype: int
        """
        top = self.path.pop()
        cur = top.right
        while cur:
            self.path.append(cur)
            cur = cur.left
        return top.val



    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())

    # O(logn), O(1), amortized O(1), O(logn)
