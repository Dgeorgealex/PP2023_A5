class Queue:
    def __init__(self):
        self.my_queue = []

    def is_empty(self):
        return len(self.my_queue) == 0

    def size(self):
        return len(self.my_queue)

    def pop(self):
        if not self.my_queue:
            return None
        x = self.my_queue[0]
        del self.my_queue[0]
        return x

    def peek(self):
        if not self.my_queue:
            return None
        return self.my_queue[0]

    def push(self, x):
        self.my_queue.append(x)


if __name__ == "__main__":
    queue = Queue()
    queue.push(4)
    queue.push(5)
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
