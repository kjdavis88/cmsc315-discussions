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
        self.internalStack = []

    def push(self, value):
        # Adds item to the end of the stack
        self.internalStack.append(value)

    def pop(self):
        # Tries to return the last item. If stack is empty, None is returned.
        try:
            return self.internalStack.pop()
        except IndexError as e:
            return None

    def peek(self):
        # Returns the top value without removing the item from the stack. Returns None if empty.
        try:
            return self.internalStack[-1]
        except IndexError as e:
            return None

    def is_empty(self):
        if len(self.internalStack) == 0:
            return True
        return False


class Queue:
    def __init__(self):
        self.internalQueue = deque()

    def enqueue(self, value):
        # Items are added to the end.
        self.internalQueue.append(value)

    def dequeue(self):
        # Tries to return the first item. If queue is empty, None is returned.
        try:
            return self.internalQueue.popleft()
        except IndexError as e:
            return None

    def front(self):
        # Returns the front item of the queue without removing it. Returns None if empty.
        try:
            return self.internalQueue[0]
        except IndexError as e:
            return None

    def is_empty(self):
        if len(self.internalQueue) == 0:
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
    # Creates stack
    test_stack = Stack()

    # Adds items to the stack
    for i in range(6):
        print(f"Current top of stack: {test_stack.peek()}")
        print(f"Pushing {i} onto stack.")
        test_stack.push(i)
        print(f"Top of stack after push: {test_stack.peek()}\n\n")

    for i in range(len(test_stack.internalStack)):
        print(f"Current top of stack: {test_stack.peek()}")
        print(f"Popped {test_stack.pop()} off of stack.")
        print(f"Top of stack after pop: {test_stack.peek()}\n\n")

    # Calling pop on an empty stack returns None.
    print(f"Empty stack pop: {test_stack.pop()}\n\n")

    # Calling peek on an empty stack returns None.
    print(f"Empty stack peek: {test_stack.peek()}\n\n")

    # Add and remove item from stack
    test_stack.push(1)
    print(f"Length of stack after push: {len(test_stack.internalStack)}\n\n")
    test_stack.pop()
    print(f"Length of stack after pop: {len(test_stack.internalStack)}\n\n")

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
    #Creates new queue
    test_queue = Queue()

    # Adds items to the queue
    for i in range(5):
        print(f"Current front of queue: {test_queue.front()}")
        print(f"Enqueueing {i} onto queue.")
        test_queue.enqueue(i)
        print(f"Front of queue after enqueue: {test_queue.front()}\n\n")

    for i in range(len(test_queue.internalQueue)):
        print(f"Current front of queue: {test_queue.front()}")
        print(f"Dequeue {test_queue.dequeue()} from queue.")
        print(f"Front of queue after dequeue: {test_queue.front()}\n\n")

    # Calling dequeue() on an empty queue returns None.
    print(f"Empty queue dequeue: {test_queue.dequeue()}\n\n")

    # Calling front() on an empty queue returns None.
    print(f"Empty queue front: {test_queue.front()}\n\n")

    # Add and remove item from queue
    test_queue.enqueue(6)
    print(f"Length of queue after enqueue: {len(test_queue.internalQueue)}\n\n")
    test_queue.dequeue()
    print(f"Length of queue after dequeue: {len(test_queue.internalQueue)}\n\n")


if __name__ == "__main__":
    main()
