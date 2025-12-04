'''
Problem Description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.


'''
class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
        if not A or A[0] == '0':
            return 0
        if len(A) == 1:
            return 1
        ways = {}
        ways[0] = 1
        if A[1] == '0':
            ways[1] = 1
        else:
            ways[1] = ways[0]
            if '10' <= A[0:2] <= '26':
                ways[1] += 1
        '''
        def decode(j):
            if j <= 0:
                return 1
            
            if j in ways:
                return ways[j]

            total_ways = 0

            if A[j] != 0:
                total_ways += decode(j-1)

            if j > 0 and '10' <= A[j-1:j+1] <= '26':
                total_ways += decode(j-2) 

            total_ways %= (10**9 + 7)    
            ways[j] = total_ways   
            return ways[j]

        return decode(len(A)-1)
        '''
        for j in range(2,len(A)):
            total_ways = 0
            if A[j] != '0' :
                total_ways += (ways[j-1] % (10**9 + 7))
            if '10' <= A[j-1:j+1] <= '26':
                total_ways += (ways[j-2] % (10**9 + 7))
            ways[j] = total_ways % (10**9 + 7)

        return ways[len(A)-1] % (10**9 + 7)