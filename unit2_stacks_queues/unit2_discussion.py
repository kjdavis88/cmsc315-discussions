"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        self.newStack = []

    def push(self, value):
        # Adds item to the end of the stack
        self.newStack.append(value)

    def pop(self):
        # Tries to return the last item. If stack is empty, None is returned.
        try:
            return self.newStack.pop()
        except IndexError as e:
            return None

    def peek(self):
        # Returns the top value without removing the item from the stack. Returns None if empty.
        try:
            return self.newStack[-1]
        except IndexError as e:
            return None

    def is_empty(self):
        if(len(self.newStack) == 0):
            return True
        return False


class Queue:
    def __init__(self):
        self.newQueue = deque()

    def enqueue(self, value):
        # Items are added to the end.
        self.newQueue.append(value)

    def dequeue(self):
        # Tries to return the first item. If queue is empty, None is returned.
        try:
            return self.newQueue.popleft()
        except IndexError as e:
            return None

    def front(self):
        # Returns the front item of the queue without removing it. Returns None if empty.
        try:
            return self.newQueue[0]
        except IndexError as e:
            return None

    def is_empty(self):
        if (len(self.newQueue) == 0):
            return True
        return False


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()
