class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
    def intersect(self, A, B):
        dictB = {}
        for val in B:
           if val in dictB:
                dictB[val] += 1
           else:
               dictB[val] = 1
        ans=[]
        for i in range(len(A)):
            if A[i] in dictB.keys() and dictB[A[i]]>0:
                ans.append(A[i])
                dictB[A[i]]-=1
        return ans

