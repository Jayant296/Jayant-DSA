'''
Problem Description

Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.


'''
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
	def solve(self, A, B, C, D):
		'''
		USING AN APPROACH LIKE DIJKSTRA'S ALGO IN WHICH WE MAINTAIN A MIN HEAP
		OF PRIME FACTORS[INITIALLY FILLED WITH THE ORIGINAL NUMBERS] AND WHENEVER
		WE FETCH A NUMBER FROM IT WE INSERT 3 NUMBERS INTO IT[NODE*P1,NODE*P2,NODE*P3]
		'''

		# PERCOLATE DOWN
        '''
    	def percolate_down(curr):
			left = 2*curr + 1
			right = 2*curr + 2
			while left < len(min_heap):
				swapped = False
				if left < len(min_heap) and right < len(min_heap):
					if min_heap[left] < min_heap[curr] or min_heap[right] < min_heap[curr]:
						if min_heap[left] < min_heap[right]:
							min_heap[left], min_heap[curr] = min_heap[curr], min_heap[left]
							curr = left
						else:
							min_heap[right], min_heap[curr] = min_heap[curr], min_heap[right]
							curr = right
						swapped = True
						left = 2*curr + 1
						right = 2*curr + 2
				elif left < len(min_heap):
					if min_heap[left] < min_heap[curr]:
						min_heap[curr], min_heap[left] = min_heap[left], min_heap[curr]
						swapped = True
						curr = left 
						left = 2*curr + 1
						right = 2*curr + 2
				if not swapped :
					break 
        '''
        # more compatible logic for percolate DOWN
        def percolate_down(curr):
            while True:
                left = 2*curr + 1
                right = 2*curr + 2
                smallest = curr

                if left < len(min_heap) and min_heap[left] < min_heap[smallest]:
                    smallest = left

                if right < len(min_heap) and min_heap[right] < min_heap[smallest]:
                    smallest = right

                if smallest != curr:
                    min_heap[curr], min_heap[smallest] = min_heap[smallest], min_heap[curr]
                    curr = smallest
                else:
                    break


		# PERCOLATE UP
		def percolate_up(curr):
			parent = (curr-1)//2
			while parent >= 0:
				if min_heap[parent] > min_heap[curr]:
					min_heap[parent], min_heap[curr] = min_heap[curr], min_heap[parent]
					curr = parent
					parent = (curr-1)//2
				else:
					break

		prime_numbers = tuple(sorted({A,B,C})) # gives the sorted tuple of numbers without duplicates(as we've used {} also)
		min_heap = [i for i in prime_numbers]
		element_check = {A,B,C}
		percolate_down(0)
		ans = []
		while min_heap:
			# deletion of minimum element
			node = min_heap[0]
			min_heap[0], min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1], min_heap[0]
			del min_heap[len(min_heap)-1]
			percolate_down(0)
			ans.append(node)
			if len(ans) == D:
				return ans

			# adding new elements
			for i in prime_numbers:
				if node*i in element_check:
					continue
				min_heap.append(node*i)
				percolate_up(len(min_heap)-1)
				element_check.add(node*i)