
class Solution:

    # Greedy Approach : T(n) : O(nlogn), S(n) : O(1)
    def solve(self, a, b):
        
        a.sort()
        b.sort()
        cnt, n = 0, len(a)

        i, j = 0, 0
        while i < n:
            if a[i] > b[j]:
                i, j = i + 1, j + 1
                cnt += 1
            else:
                i += 1
    
        return cnt