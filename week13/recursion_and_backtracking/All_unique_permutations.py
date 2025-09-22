class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def gen(self, A, curr_arr, curr_index, frequency, ans):
        n = len(A)
        if curr_index == n:
            ans.append(curr_arr[:])
            return
        for key in frequency:
            if frequency[key] == 0:
                continue
            curr_arr[curr_index] = key
            frequency[key]-=1
            self.gen(A, curr_arr, curr_index+1, frequency, ans) 
            frequency[key]+=1
    def permute(self, A):
        curr_arr = []
        frequency = dict()
        ans=[]
        for i in range(len(A)):
            if A[i] in frequency:
                frequency[A[i]] += 1
            else:
                frequency[A[i]] = 1
        curr_arr = [0] * len(A)
        self.gen(A, curr_arr, 0, frequency, ans)
        return ans