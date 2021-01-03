

class Solution:

    # T(n) : O(n + n), S(n) : O(1) 
    def solve(self, heights):
        
        n, res, max_ = len(heights), [], -1

        for i in range(n - 1, -1, -1):
            if heights[i] > max_:
                res.append(i)
                max_ = heights[i]
        
        return res[::-1]