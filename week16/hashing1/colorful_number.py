class Solution:
	# @param A : integer
	# @return an integer
    def colorful(self, A):
        digits = [ int(i) for i in str(A)]
        n = len(str(A))
        ans = dict()
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= digits[j]
                if prod in ans:
                    return 0
                else:
                    ans[prod] = 1
        return 1