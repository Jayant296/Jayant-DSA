'''
Problem Description

Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

'''


from collections import deque
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        # # unweighted so we can use BFS.
        # def continuous_roll(i,j,roll_direc):
        #     count = 0
        #     while 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 0:
        #         count += 1
        #         i += roll_direc[0]
        #         j += roll_direc[1]
        #     return count

        # queue = deque()
        # neighbours = [(0,-1), (0,1), (-1,0), (1,0,)]

        # queue.append(((B[0],B[1]),0))
        # while queue:
        #     node = queue.popleft()
        #     if (node[0][0],node[0][1]) == (C[0],C[1]):
        #         return node[1]

        #     for i in neighbours:
        #         m = node[0][0] + i[0]
        #         n = node[0][1] + i[1]
        #         if 0 <= m < len(A) and 0 <= n < len(A[0]) and A[m][n] != 1:
        #             queue.append(((m,n),node[1] + 1 + 2*continuous_roll(m,n,i)))
        #             A[m][n] = 1

        # return -1
        '''
        can't apply the bfs because here the weight of each edge is not same,
        as we can see that the weight of each edge represents the no. of empty cells
        travelled by the ball to stop at a particualar location.
        the ans only returns a +ve value if and only if the ball exactly stops at a locations
        through any path not just pass over it, if no valid path to stop at the destination is
        found then we return -1.
        so we need the Dijkstra's here.

        '''
        # dijkstra's algo
        neighbours = [(0,-1), (0,1), (-1,0), (1,0,)]
        min_heap = []
        def percolate_down(curr): # for maintaining min heap after deletion
            left = 2*curr + 1
            right = 2*curr + 2

            while left < len(min_heap):
                swapped = False
                if left < len(min_heap) and right < len(min_heap):
                    if min_heap[left][1] < min_heap[curr][1] or min_heap[right][1] < min_heap[curr][1]:
                        if min_heap[left][1] < min_heap[right][1]:
                            min_heap[curr], min_heap[left] = min_heap[left], min_heap[curr]
                            curr = left
                        else:
                            min_heap[curr], min_heap[right] = min_heap[right], min_heap[curr]
                            curr = right
                        swapped = True
                        left = 2*curr + 1
                        right = 2*curr + 2
                elif left < len(min_heap):
                    if min_heap[left][1] < min_heap[curr][1]:
                        min_heap[curr], min_heap[left] = min_heap[left], min_heap[curr]
                        swapped = True
                        curr = left 
                        left = 2*curr + 1
                        right = 2*curr + 2
                if not swapped:
                    break

        def percolate_up(curr): # for maintaining min heap after the insertion
            parent = (curr - 1)//2
            while parent >= 0:
                if min_heap[curr][1] < min_heap[parent][1]:
                    min_heap[curr], min_heap[parent] = min_heap[parent], min_heap[curr]
                    curr = parent 
                    parent = (curr - 1)//2
                else:
                    break
        
        def continuous_roll(i,j,direction): # to return the final node index & path value, where ball stops to push into min heap.
            i += direction[0]
            j += direction[1]
            count = 0
            while 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 0:
                count += 1
                i += direction[0]
                j += direction[1]
            return (i-direction[0],j-direction[1],count)

        dist = [[float('inf') for _ in range(len(A[0]))] for _ in range(len(A))] # for storing and maintaing the minimum distances from the source to each cell.
        min_heap.append((B,0))
        while min_heap:
            # removing node from min heap as its the best path now
            node = min_heap[0]
            min_heap[0], min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1], min_heap[0]
            del min_heap[len(min_heap)-1]
            percolate_down(0)
            
            if node[0] == C: # node == destination, then stop and return ans.
                return node[1]
            
            if dist[node[0][0]][node[0][1]] < node[1]: # if we already have a better ans than this node's path then skip the traversal.
                continue

            for i in neighbours:
                m = node[0][0] + i[0]
                n = node[0][1] + i[1]

                if 0 <= m < len(A) and 0 <= n < len(A[0]) and A[m][n] == 0:
                    x,y,rolls = continuous_roll(m,n,i)
                    if dist[x][y] <= node[1] + 1 + rolls: # if we already have a better ans than this node's path then skip the pushing onto the min heap.
                        continue
                    dist[x][y] = node[1] + 1 + rolls
                    min_heap.append(([x,y],node[1]+rolls+1))
                    percolate_up(len(min_heap)-1)
        
        return -1