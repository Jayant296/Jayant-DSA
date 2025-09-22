class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def max_books(self, A, students, st, end, ans):
        if st>end:
            return ans
        mid= (st + end)//2
        count= 1
        pages=0
        feasible=True
        for i in range(len(A)):
            if A[i]>mid:
                feasible=False
                break
            if pages+A[i]>mid:
                count+=1
                pages=A[i]
                if count>students:
                    feasible=False
                    break
            else:
                pages+=A[i]
        if feasible:
            ans = min(ans,mid)
            return self.max_books(A, students, st, mid-1, ans)
        else:
            return self.max_books(A, students, mid+1, end, ans)
	def books(self, A, B):
        n= len(A)
        if B>len(A):
            return -1
        return self.max_books(A, B, max(A), sum(A), float('inf'))