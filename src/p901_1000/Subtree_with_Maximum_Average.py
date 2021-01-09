"""
Problem : https://binarysearch.com/problems/Subtree-with-Maximum-Average
"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # T(n) : O(n),  S(n) : O(h) , h = height of binary tree
    def solve(self, root):
        
        def subtree(root):

            if not root:
                return (0, 0, 0)
            elif root.left == None and root.right == None:
                return (root.val, 1, root.val)

            left = subtree(root.left)
            right = subtree(root.right)

            sum_ = root.val + left[0] + right[0]
            count_ = 1 + left[1] + right[1]
            max_average = max(left[2], max(right[2], sum_ / count_))
            return (sum_, count_, max_average)

        return subtree(root)[2]