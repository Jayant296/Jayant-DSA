'''
Problem Description

Given an integer array A of size N.
You have to find the product of the three largest integers in array A from range 1 to i, where i goes from 1 to N.

Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i in B should be -1.

'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # creating min a heap of size 3
        def percolate_down(curr):
            left = 1
            right = 2
            if A[curr] > prod[0]:
                prod[0] = A[curr]
            if prod[left] < prod[0] or prod[right] < prod[0]:
                if prod[left] < prod[right]:
                    prod[left], prod[0] = prod[0], prod[left]
                else:
                    prod[right], prod[0] = prod[0], prod[right]
            return prod[0]*prod[1]*prod[2]

        first = min(A[0], A[1])
        second = A[0] if first == A[1] else A[1] 
        prod = [first, second]
        if first > A[2]:
            prod.append(first)
            prod[0] = A[2]
        else:
            prod.append(A[2])
        ans = [-1, -1, A[0]*A[1]*A[2]]
        if len(A) <= 3:
            return ans
        for i in range(3, len(A)):
            ans.append(percolate_down(i))
        return ans




