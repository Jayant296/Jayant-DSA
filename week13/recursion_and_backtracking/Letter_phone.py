class Solution:
	# @param A : string
	# @return a list of strings

    def gen(self, A, frequency, curr_str, starting_index, ans):
        n = len(A)
        if len(curr_str) == n:
            ans.append(curr_str)
        else:
            for i in range(len(frequency[int(A[starting_index])])):
                new_str = curr_str + frequency[int(A[starting_index])][i] # made new_str to store values ans recursion only store remembers lists and dictionaries.
                self.gen(A, frequency, new_str, starting_index + 1, ans)
        return 

    def letterCombinations(self, A):
        ans = []
        frequency = {
            0 : '0', 1 : '1', 2 : 'abc', 3 : 'def', 4 : 'ghi', 5 : 'jkl', 
            6 : 'mno', 7 : 'pqrs', 8 : 'tuv', 9 : 'wxyz'
        }
        self.gen(A, frequency, '', 0, ans)
        return ans