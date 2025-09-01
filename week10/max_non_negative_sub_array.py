class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        """
        Finds the maximum sum sub-array of non-negative numbers from a list of integers.

        Args:
            A: The input list of integers.

        Returns:
            A list representing the required sub-array. Returns an empty list
            if no non-negative numbers are present.
        """
        n = len(A)
        if n == 0:
            return []

        # Variables to track the current non-negative sub-array
        current_sum = 0
        current_start_index = 0
        
        # Variables to track the best non-negative sub-array found so far
        max_sum = -1  # Initialize with a value less than any possible sum (e.g., -1)
        max_start_index = -1
        max_end_index = -1
        
        for i in range(n):
            # If the current element is non-negative, add it to the current sum
            if A[i] >= 0:
                current_sum += A[i]
            else:
                # A negative number marks the end of a non-negative sub-array
                # Now, we compare the current sub-array with the max one found so far
                # We use float('inf') for sum to handle large numbers.
                # Using -1 for max_sum works because all non-negative sums are >= 0.
                
                # Tie-breaking rule 1: Compare sums
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_start_index = current_start_index
                    max_end_index = i
                
                # Tie-breaking rule 2: Compare lengths (if sums are tied)
                elif current_sum == max_sum:
                    current_length = i - current_start_index
                    max_length = max_end_index - max_start_index
                    if current_length > max_length:
                        max_sum = current_sum
                        max_start_index = current_start_index
                        max_end_index = i
                
                # Reset current variables for the next sub-array
                current_sum = 0
                current_start_index = i + 1

        # After the loop, there might be a trailing non-negative sub-array
        # that hasn't been compared yet. We need one final check.
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = current_start_index
            max_end_index = n
        elif current_sum == max_sum:
            current_length = n - current_start_index
            max_length = max_end_index - max_start_index
            if current_length > max_length:
                max_sum = current_sum
                max_start_index = current_start_index
                max_end_index = n
        
        # Return the slice of the original array
        if max_start_index == -1:
            return []
        
        return A[max_start_index:max_end_index]