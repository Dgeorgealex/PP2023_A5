class Stack:
    def __init__(self):
        self.my_stack = []

    def is_empty(self):
        return len(self.my_stack) == 0

    def size(self):
        return len(self.my_stack)

    def peek(self):
        if not self.my_stack:
            return None
        return self.my_stack[-1]

    def pop(self):
        if not self.my_stack:
            return None
        x = self.my_stack[-1]
        del self.my_stack[-1]
        return x

    def push(self, x):
        self.my_stack.append(x)


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(5)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print(stack.is_empty())

