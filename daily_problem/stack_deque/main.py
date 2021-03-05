# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.
#
# Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
#
# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
#
# Hint: Try working backwards from the end state.
import math as math
from collections import deque

def backwards(stack):
    sz = len(stack)
    if sz <= 2:
        return stack

    queue = deque()
    for i in range(sz-1): #Pop till the first element is only staying
        queue.append(stack.pop())

    stack.append(queue.popleft()) #Add the last element of the list to the second position
    result = stack
    stack = []

    # Put back in order the rest of the queue content and put it on the stack
    for i in range(sz-2):
        stack.append(queue.popleft())

    for i in range(sz-2):
        queue.append(stack.pop())

    for i in range(sz-2):
        stack.append(queue.popleft())

    # print('Current result: ', result)
    # print('Left stack: ', stack)

    # Call recursively on the reduced stack
    result += backwards(stack)
    return result


given = list(range(15))
print(backwards(given))
