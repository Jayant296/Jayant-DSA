class Solution:
	# @param A : tuple of integers
	# @return an integer
    def longestConsecutive(self, A):
        set_A = set()
        for i in A:
            set_A.add(i)
        ans = float('-inf')
        for i in A:
            if i+1 not in set_A:
                j = i
                count = 1
                while j-1 in set_A:
                    count += 1
                    j -= 1
                ans = max(ans, count)
        return ans