class Solution:
	# @param A : list of integers
	# @return a list of integers
    def subUnsort(self, A):
        hashA = dict()
        for i in A:
            if i in hashA:
                hashA[i] += 1
            else:
                hashA[i] = 1
        maxA = max(A)
        minA = min(A)
        index = 0
        curr_element = minA
        st, end = -1, -1
        while curr_element <= maxA:
            if curr_element in hashA:
                if A[index] != curr_element:
                    if st == -1:
                        st = index
                        end = index
                    else:
                        end = index
                index += 1
                hashA[curr_element] -= 1
                if hashA[curr_element] == 0:
                    curr_element += 1
                    continue
            else:
                curr_element+=1
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return [st, end]
        return [-1]
