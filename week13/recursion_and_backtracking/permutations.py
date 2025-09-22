class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def gen(self, A, curr_arr, curr_index, used, ans):
        '''
        args:
        A : given array
        curr_arr : current array for storing permutations
        curr_index : current index of permutation 
        used : indicates that which lement is has been already used to avoid duplicates
        ans : empty list to store all permutations.

        learning : always append the copy of the current array in the ans, as it 
        changes the previously stored values in the ans if changes made in future
        as the curr_arr points to the same address.

        '''
        n = len(A)
        if curr_index == n:

            ans.append(curr_arr[:])
            return 
        for i in range(n):
            if used[i] == 1:
                continue
            curr_arr[curr_index] = A[i]
            used[i] = 1
            self.gen(A, curr_arr, curr_index+1, used, ans)
            used[i] = 0
        return ans
    def permute(self, A):
        curr_arr = []
        used = []
        for i in range(len(A)):
            curr_arr.append(0)
            used.append(0)
        return self.gen(A, curr_arr, 0, used, [])