'''
Docstring for Gym_Trainer
Problem Description

You are the trainer of a gym and there are A people who come to your gym.

Some of them are friends because they walk together, and some of them are friends because they talk together.
But people become possessive about each other, so a person cannot walk with one friend and talk with another. Although he can walk with two or more people or talk with two or more people.

You being the trainer, decided to suggest each one of the 2 possible diets. But friends, being friends will always have the same diet as all the other friends are having.

Find and return the number of ways you can suggest each of them a diet.

As the number of ways can be huge, return the answer modulo 109+7.

NOTE: If there is any person who walks with one person and talks with the another person, then you may return 0.

'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        '''
        to find the connected components in this question:
        1.) join all by doing union through roots and add all elements in a set for taking unique or actual elements .
        2.) now for each element of the involved set find root and add it to the root set for uniqueness.
        3.) also there may be some people who are not friends of anyone so they are unique connected components [i.e. total - len(involved) ]
        4.) add len(roots) and singles.
        '''
        # initial check for no overlapping between groups
        walk_together = set()
        talk_together = set()

        for u,v in B:
            walk_together.add(u)
            walk_together.add(v)

        for u,v in C:
            talk_together.add(u)
            talk_together.add(v)

        if walk_together & talk_together:
            return 0
        
        # finding the connected components in both groups by using dsu
        def union_by_height(a,b):
            if a == b:
                return

            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[b] = a
                rank[a] += 1
            return

        def find_root_by_compression(x):
            if parent[x] == x:
                return parent[x]
            else:
                parent[x] = find_root_by_compression(parent[x])
            return parent[x]
        
        parent = [i for i in range(A)]
        rank = [0]*A

        # making connected components or joining common groups
        involved = set()
        for u,v in B:
            ru = find_root_by_compression(u-1)
            rv = find_root_by_compression(v-1)
            involved.add(u-1)
            involved.add(v-1)
            union_by_height(ru,rv)
        
        for u,v in C:
            ru = find_root_by_compression(u-1)
            rv = find_root_by_compression(v-1)
            involved.add(u-1)
            involved.add(v-1)
            union_by_height(ru,rv)
        
        # finding roots
        roots = set()
        for i in involved:
            roots.add(find_root_by_compression(i))
        
        isolated = A - len(involved)
        total_components = len(roots) + isolated
        return (2**total_components) % (10**9 + 7)