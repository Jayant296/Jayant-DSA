'''
Problem Description

You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.

NOTE:

Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
        ways = [0 for _ in range(B+1)]
        A.sort()
        ways[0] = 1
        
        # now we'll simply iterate over the sums from 1 till B , that is we'll that whether we can make the sum from the given set of coins or not.
        # for i in range(B+1): # particular value of ways to create i.
        #     for j in range(len(A)):# jth coin.
        #         if A[j] > i:
        #             break
        #         ways[i] += ways[i-A[j]]
        '''
        this will give us the permutations, as we are using calculating ways[i] from n coins.
        But we want the combinations so now we will calculate ways[i] by not considering relative order.
        '''        
        for j in range(len(A)):
            for i in range(A[j],B+1):
                ways[i] += ways[i-A[j]]
            
        return ways[B] % (10**6 + 7)

        