
class Solution:
    def solve(self, s):
        
        cnt = 0
        for brace in s:
        	if cnt < 0 : return False
        	if brace == '(':
        		cnt += 1
        	else :
        		cnt -= 1

        return cnt == 0