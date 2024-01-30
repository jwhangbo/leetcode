# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:
    # the push, pop and top methods can all be done through Python's built-in methods
    # however, getting the minimum value in a stack is not a feature within the built-in methods
    # the requirement of every function running at O(1) time prevents the use of iterating through the stack to find the min
    # using a number to save the minimum value after each value is pushed into the stack cannot work
    # this is because the number does not track the count - thus, duplicate values will cause this method to fail
    # therefore, a separate min stack must be created to track the minimum value within the stack on a node by node basis

    # for instance, if the values 0, -2 and -1 were pushed into the stack in that order, the following would occur
    # for 0, the minimum value is the first value pushed, so the min value of 0 will be pushed into the min stack
    # for -2, the new minimum value is -2, so it will be pushed into the min stack
    # however, for -1, the minimum value is still -2, so the latter will be pushed into the min stack
    # as long as the two stacks remain in sync, the min stack will be able to return the minimum value of the stack

    def __init__(self):
        # create the two stacks
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        # for the stack, append the value
        self.stack.append(val)

        # for the min stack, append the minimum value
        # the minimum value is found by comparing the current value to the top of the min stack, as long as min stack has a value
        minval = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)

    def pop(self) -> None:
        # whenever the stack is popped, the min stack must also be popped to be in sync
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        # the built-in method can be used to get the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # the built-in method can be used to get the top of the min stack
        return self.minstack[-1]