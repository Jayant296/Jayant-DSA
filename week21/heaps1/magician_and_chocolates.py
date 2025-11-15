'''
Problem Description

Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it, then the magician will fill the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that the kid can eat in A units of time.

NOTE:

floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7
'''
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
        
        # # percolate down
        # new_B = B[:]
        # def percolate_down(curr):
        #     left = 2*curr + 1
        #     right = 2*curr + 2
        #     while 2*curr + 1 < len(new_B):
        #         swapped = False
        #         if left < len(new_B) and right < len(new_B):
        #             if new_B[left] > new_B[curr] or new_B[right] > new_B[curr]:
        #                 if new_B[left] > new_B[right]:
        #                     new_B[left], new_B[curr] = new_B[curr], new_B[left]
        #                     curr = left
        #                 else:
        #                     new_B[right], new_B[curr] = new_B[curr], new_B[right]
        #                     curr = right 
        #                 swapped = True
        #                 left = 2*curr + 1
        #                 right = 2*curr + 2
        #         elif left < len(new_B):
        #             if new_B[left] > new_B[curr]:
        #                 new_B[left], new_B[curr] = new_B[curr], new_B[left]
        #                 curr = left
        #                 swapped = True
        #                 left = 2*curr + 1
        #                 right = 2*curr + 2 
        #         if not swapped:
        #             break
        
        # # creating the max heap 
        # for i in range((len(new_B) - 1)//2 , -1 , -1):
        #     percolate_down(i)
        
        # # doing A operations
        # ans = 0
        # for a in range(A):
        #     ans += new_B[0]
        #     new_B[0] //= 2
        #     percolate_down(0)
        
        # return ans % (10**9 + 7)
        '''
        the above solution is good but not suitable for the large testceses, 
        so we need to apply the pyhton' s standard heapq method .
        '''
        import heapq
        
        MOD = 10**9 + 7
        
        # indirectly creating max_heap
        max_heap = [-x for x in B]
        heapq.heapify(max_heap)

        chocolates = 0
        for _ in range(A):
           
            # retmoving max element
            x = -heapq.heappop(max_heap)
            
            chocolates += x 
            
            # adding back in heap
            heapq.heappush(max_heap, -(x//2))

        return chocolates % MOD