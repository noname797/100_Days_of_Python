class DataStructures:
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, inn):
            self.stack.append(inn)

        def pop(self):
            element = self.stack[-1]
            self.stack = self.stack[:-1]
            return element

        def top(self):
            if len(self.stack) == 0:
                return "Stack is empty"

            else:
                return self.stack[-1]

    class Queue:
        def __init__(self):
            self.q = []

        def enq(self, inn):
            self.q.append(inn)

        def deq(self):
            element = self.q[0]
            self.q = self.q[1:]
            return element

        def top(self):
            if len(self.q) == 0:
                return "Queue is empty"
            else:
                return self.q[0]



