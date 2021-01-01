

class Solution:
    def solve(self, nums, k):
        
        lookup = set()
        for val in nums:
        	if k - val in lookup:
        		return True
        	lookup.add(val)

        return False