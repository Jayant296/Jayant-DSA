class Solution:
    # @param A : integer
    # @return a list of list of strings
    def gen(self, N, curr_arr, curr_index, ans):
        if curr_index == N:
            ans.append(curr_arr[:])
        else:
            for index in range(N):
                insertion_check = True
                i, j = curr_index - 1, index - 1
                while i >= 0 and j >= 0 and insertion_check == True: # LOOP FOR LEFT DIAGONAL
                    if curr_arr[i][j] == 'Q':
                        insertion_check = False
                        break
                    else:
                        i -= 1
                        j -= 1
                i, j = curr_index - 1, index + 1 
                while i >= 0 and j < N and insertion_check == True: # LOOP FOR RIGHT DIAGONAL
                    if curr_arr[i][j] == 'Q':
                        insertion_check = False
                        break
                    else:
                        i -= 1
                        j += 1
                i, j = curr_index - 1, index
                while i >= 0 and insertion_check == True: # LOOP FOR SAME COLUMN
                    if curr_arr[i][j] == 'Q':
                        insertion_check = False
                        break
                    else:
                        i -= 1
                if insertion_check == True:
                    for i in range(N):
                        if i == index:
                            curr_arr[curr_index] = curr_arr[curr_index] + 'Q'
                        else:
                            curr_arr[curr_index] = curr_arr[curr_index] + '.'  
                    self.gen(N, curr_arr, curr_index + 1, ans)
                    curr_arr[curr_index] = ''
                else:
                    continue

    def solveNQueens(self, A):
        curr_arr = [''] * A
        ans = []
        self.gen(A, curr_arr, 0, ans)
        return ans