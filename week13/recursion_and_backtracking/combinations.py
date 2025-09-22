class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	def gen(self, A, B, curr_arr, curr_index, starting_index, ans):
		if curr_index == B:
			ans.append(curr_arr[:])
			return 
		else:
			for i in range(starting_index,len(A)):
				curr_arr[curr_index] = A[i]
				self.gen(A, B, curr_arr, curr_index+1, i+1, ans)
			return 
	def combine(self, A, B):
		arr = [i for i in range(1,A+1)]
	    ans = []
	    curr_arr = [0]*B
		self.gen(arr, B, curr_arr, 0, 0, ans)
		return ans