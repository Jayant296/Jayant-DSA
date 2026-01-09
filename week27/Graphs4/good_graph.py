'''
Docstring for good_graph
Problem Description

Given a directed graph of N nodes where each node is pointing to exactly one of the N nodes (can possibly point to itself). Ishu, the coder, is bored and he has discovered a problem out of it to keep himself busy. Problem is as follows:

A node is 'good' if it satisfies one of the following:

1. It is the special node (marked as node 1)
2. It is pointing to the special node (node 1)
3. It is pointing to a good node.
Ishu is going to change pointers of some nodes to make them all 'good'. You have to find the minimum number of pointers to change in order to make all the nodes good (Thus, a Good Graph).

NOTE: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        '''
        applying DSU logic 
        

        def find_root(x): # finds root(x) through compression logic
            if parent[x] == x:
                return parent[x]

            parent[x] = find_root(parent[x])
            return parent[x]

        def union(a,b):
            ra = find_root(a)
            rb = find_root(b)
            
            if ra != rb:
                parent[ra] = rb
            
            return

        def is_root_0(x):
            if parent[x] == x:
                return False
            elif parent[x] == 0:
                return True
            else:
                return is_root_0(parent[x])

        parent = [i for i in range(len(A))]
        rank = [0 for _ in range(len(A))]
        roots = set()

        for i in range(len(A)):
            union(i,A[i]-1)

        # counting how many components does'nt point to root of 0
        for i in range(len(A)):
            if is_root_0(i):
                continue
            ri = find_root(i)
            if ri != 0 and ri not in roots : 
                roots.add(ri)
                
        return len(roots)

        UNABLE TO SOLVE THROUGH DSU
        '''

        # applying dfs
        '''
        iterating over each node and checking whether we can visit node 1 
        from it or not .
        applied special cases for cycle detection by using special visited array 
        named as 'state' 
        '''

        n = len(A)
        # 0 means unvisited, 1 means visiting and 2 means visited.
        state = [0]*n

        def dfs(u):
            state[u] = 1
            v = A[u] - 1

            # unvisited
            if state[v] == 0:
                dfs(v)

            # visiting
            elif state[v] == 1:
                # cycle detected
                # checking for node 1 or 0 index
                curr = v
                has_node1 = False

                while True:
                    if curr == 0:
                        has_node1 = True
                    else:
                        curr = A[curr] - 1 
                    if curr == v:
                        break

                if not has_node1:
                    self.oprs += 1
            
            state[u] = 2
        
        self.oprs = 0

        for i in range(n):
            if state[i] == 0:
                dfs(i)
        
        return self.oprs