'''
Docstring for batches
Problem Description

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.


'''
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        # Typical connected components problem
        '''
        we are going to use the BFS here, as we just need to count the number
        of groups fulfilling the criteria of company , we traverse through all the nodes 
        and maintain a current sum, if its greater than or equal to the D or not.
        '''
        adj_list = {i:[] for i in range(1,A+1)}
        for i in range(len(C)):
            adj_list[C[i][0]].append(C[i][1])
            adj_list[C[i][1]].append(C[i][0])
        visited = [0 for _ in range(A)]
        selected_grps = 0
        
        for k in range(1,A+1):
            if visited[k-1]:
                continue
            queue = deque()
            queue.append(k)
            current_sum = B[k-1]
            visited[k-1] = 1
            while queue:
                node = queue.popleft()
                for i in adj_list[node]:
                    if visited[i-1]:
                        continue
                    queue.append(i)
                    visited[i-1] = 1
                    current_sum += B[i-1]
            if current_sum >= D:
                selected_grps += 1
        
        return selected_grps