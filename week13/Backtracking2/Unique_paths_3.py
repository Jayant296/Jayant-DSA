class Solution:
    # @param A : list of list of integers
    # @return an integer
    def gen(self, A, x, y, visited_zeros, total_zeros):
        rows = len(A)
        col = len(A[0])
        # if we reach the end
        if A[x][y] == 2:
            if visited_zeros == total_zeros:
                self.ans += 1
                return
        # mark the current cell as visited
        temp = A[x][y]
        A[x][y] = -1

        # explore neighbours left, right up, down.
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < col:
                if A[nx][ny] == 0:
                    self.gen(A, nx, ny, visited_zeros+1, total_zeros)
                if A[nx][ny] == 2:
                    self.gen(A, nx, ny, visited_zeros, total_zeros)
        # Backtrack
        A[x][y] = temp
        return 

    def solve(self, A):
        start = None
        total_zeros = 0
        self.ans = 0
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 1:
                    start = (row, col)
                if A[row][col] == 0:
                    total_zeros += 1 
        self.gen(A, start[0], start[1], 0, total_zeros) 
        return self.ans