"""
Problem Description

Given an array of integers A and an integer B. You must modify the array exactly B number of times. In a single modification, we can replace any one array element A[i] by -A[i].

You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # applying percolate down
        def percoalte_down(curr):
            left = 2*curr + 1
            right = 2*curr + 2
            while 2*curr + 1 < len(A) :
                swapped = False
                if left < len(A) and right < len(A):
                    if A[curr] > A[left] or A[curr] > A[right]:
                        if A[left] < A[right]:
                            A[curr], A[left] = A[left], A[curr]
                            curr = left
                        else:
                            A[curr], A[right] = A[right], A[curr]
                            curr = right
                        swapped = True
                        left = 2*curr + 1
                        right = 2*curr + 2 
                elif left < len(A):
                    if A[curr] > A[left]:
                        A[curr], A[left] = A[left], A[curr]
                        curr = left
                        swapped = True
                        left = 2*curr + 1
                        right = 2*curr + 2
                if not swapped:
                    break

        # creating a min heap
        for i in range((len(A)-1)//2, -1, -1):
            percoalte_down(i)

        # applying the b operations and also doing percolate down for fetching the min value at top
        for b in range(B):
            A[0] = (-1)*A[0]
            percoalte_down(0)
        
        ans = 0
        for i in A:
            ans += i

        return ans
        
