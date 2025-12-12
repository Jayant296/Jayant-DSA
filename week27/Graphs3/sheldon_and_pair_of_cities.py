'''
Docstring for sheldon_and_pair_of_cities
Problem Description

Sheldon lives in a country with A cities (numbered from 1 to A) and B bidirectional roads.

Roads are denoted by integer array D, E and F of size M, where D[i] and E[i] denotes the cities and F[i] denotes the distance between the cities.

Now he has many lectures to give in the city and is running short of time, so he asked you C queries, for each query i, find the shortest distance between city G[i] and H[i].

If the two cities are not connected then the distance between them is assumed to be -1.


'''
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : list of integers
	# @param E : list of integers
	# @param F : list of integers
	# @param G : list of integers
	# @param H : list of integers
	# @return a list of integers
	def solve(self, A, B, C, D, E, F, G, H):
        # applying floyd warshall
        '''
        IMPORTANT POINT 
        there can be multiple edges so handle that as well
        '''
        dist = [[0 for _ in range(A)] for _ in range(A)]
        for i in range(len(D)):
            # if there is a self loop then mark it as distace 0, demanded by a test case further and also its pretty intuitive that if a person is already in a city then he needs zero units of time to reach his place. 
            if D[i] == E[i]:
                dist[D[i]-1][E[i]-1] = 0
                continue
            if dist[D[i]-1][E[i]-1] == 0:
                dist[D[i]-1][E[i]-1] = F[i] # for 0 based indexing using -1 
                dist[E[i]-1][D[i]-1] = F[i]
            else:
                dist[D[i]-1][E[i]-1] = min(dist[D[i]-1][E[i]-1],F[i])
                dist[E[i]-1][D[i]-1] = min(dist[E[i]-1][D[i]-1],F[i])

        for i in range(A):
            for j in range(A):
                if i != j and dist[i][j] == 0:
                    dist[i][j] = float('inf')
        
        # main loop
        for k in range(A):
            for i in range(A):
                for j in range(A):
                    if i != j:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = []
        for i in range(C):
            if dist[G[i]-1][H[i]-1] == float('inf'):
                ans.append(-1)
            else:
                ans.append(dist[G[i]-1][H[i]-1])
        
        return ans