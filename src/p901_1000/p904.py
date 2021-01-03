
class Solution:

    # Binary Seach : T(n) : O(nlogn), S{n} : O(1)
    def solve(self, piles, k):

        def check(piles, t): 
            cnt = 0
            for i in range(len(piles)):
                cnt += ceil(piles[i] / t)
            return cnt

        l, r = 1, 100000
        while l < r:
            mid = l + (r - l) // 2

            if check(piles, mid) <= k :
                r = mid
            else:
                l = mid + 1

        return l
