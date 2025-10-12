'''
Problem Description

Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.

'''
class MinStack:

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if len(self.stack) == 0 :
            self.stack.append(x)
            self.min_val = x
        elif x >= self.min_val:
            self.stack.append(x)
        else:
            top = 2*x - self.min_val
            self.stack.append(top)
            self.min_val = x

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return
        else:
            if self.stack[-1] >= self.min_val :
                del self.stack[-1]
            else:
                self.min_val = 2*self.min_val - self.stack[-1]
                del self.stack[-1]

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            if self.stack[-1] >= self.min_val:
                return self.stack[-1]
            else:
                return self.min_val

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.min_val
    
    def __init__(self):
        self.stack = []
        self.min_val = None