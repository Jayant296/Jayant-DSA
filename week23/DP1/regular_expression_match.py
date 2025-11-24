'''
Problem Description

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).



The matching should cover the entire input string (not partial).


'''
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
		dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
		for j in range(len(A) + 1):
			dp[0][j] = 0
		flag = True
		for i in range(1,len(B) + 1):
			if B[i-1] != '*':
				flag = False
			if not flag :
				dp[i][0] = 0
			else:
				dp[i][0] = 1
		dp[0][0] = 1

        # #top-down
		# def check(i,j):
		# 	if i == 0 and j == 0 :
		# 		return 1
        #     if i == 0:
        #         return 0
        #     if j == 0: # for handling the edge case of '*' in the starting.
        #         return dp[i][j] 

		# 	if dp[i][j] != -1:
		# 		return dp[i][j]

		# 	if B[i-1] != '*' and B[i-1] != '?':
		# 		if B[i-1] == A[j-1]:
		# 			dp[i][j] = check(i-1,j-1)
		# 		else:
		# 			dp[i][j] = 0
		# 	elif B[i-1] == '*':
		# 		if check(i-1,j-1) == 1 or check(i,j-1) == 1 or check(i-1,j) == 1:
		# 			dp[i][j] = 1
		# 		else:
		# 			dp[i][j] = 0
		# 	elif B[i-1] == '?':
		# 		dp[i][j] = check(i-1,j-1)
			
		# 	return dp[i][j]

		# return check(len(B),len(A))
        '''
        top-down not worling for large test-cases so using bottom up.
        '''
        # bottom-up
        for i in range(1,len(B)+1):
            for j in range(1,len(A)+1):
                if B[i-1] != '*' and B[i-1] != '?':
                    if B[i-1] == A[j-1]:
                        dp[i][j] = dp[i-1][j-1] 
                    else:
                        dp[i][j] = 0
                elif B[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif B[i-1] == '*':
                    if dp[i-1][j-1] == 1 or dp[i-1][j] == 1 or dp[i][j-1] == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
        return dp[len(B)][len(A)]
 