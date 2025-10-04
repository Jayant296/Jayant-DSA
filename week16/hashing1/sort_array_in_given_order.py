class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def quick_sort(self, A, st, end):
        if st < end:
            pivot = A[end]
            j = st - 1
            for i in range(st, end):
                if A[i] < pivot:
                    j += 1
                    A[i], A[j] = A[j], A[i]               
            j += 1
            A[end], A[j] = A[j], A[end]
            self.quick_sort(A, st, j-1)
            self.quick_sort(A, j+1, end)
        return A             
    def solve(self, A, B):
        A = self.quick_sort(A, 0, len(A) - 1)
        frequency_A = dict()
        for i in A:
            if i in frequency_A:
                frequency_A[i] += 1
            else:
                frequency_A[i] = 1
        k = 0
        for j in B:
            if j in frequency_A :
                while frequency_A[j] > 0:
                    A[k] = j
                    k += 1
                    frequency_A[j] -= 1
        for i in frequency_A:
            if frequency_A[i] != 0:
                while frequency_A[i] > 0:
                    A[k] = i
                    k += 1
                    frequency_A[i] -= 1
        return A