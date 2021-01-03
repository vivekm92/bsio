
class Solution:

	# T(n) : O(n), S(n) : O(1)
    def solve(self, votes):

        n = len(votes)        
        def check(votes, idx):
            if idx < 0 or idx >= n:
                return idx
            
            votes[idx] = check(votes, votes[idx])
            return votes[idx]

        return sum([check(votes, i) < 0 for i in range(n)])