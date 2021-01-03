# Problem : [906] https://binarysearch.com/problems/Sum-of-Two-Numbers-in-BSTs

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # T(n) : O(n), S(n) : O(n)
    def solve(self, a, b, target):

        def inOrder(t):

            traversal, stack = [], []
            while t or stack:
                while t:
                    stack.append(t)
                    t = t.left
                
                t = stack[-1]
                stack.pop()
                traversal.append(t.val)
                t = t.right
            
            return traversal

        arr1, arr2 = inOrder(a), inOrder(b)

        n, m = len(arr1), len(arr2)
        i, j = 0, m - 1
        while i < n and j >= 0:
            sum_ = arr1[i] + arr2[j]
            if sum_ == target:
                return True
            elif sum_ > target:
                j -= 1
            else :
                i += 1

        return False
            