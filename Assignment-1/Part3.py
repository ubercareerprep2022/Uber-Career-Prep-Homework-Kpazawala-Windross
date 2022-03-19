class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        #self.stack.append(value)
        self.stack += [value]

    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack[-1]
            #self.stack.pop(-1)
            self.stack = self.stack[0:-1]
            return temp

    def top(self):
        return self.stack[0]

    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)

    def min(self):
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return None


class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, value):
        #self.queue.insert(0, value)
        self.queue = [value] + self.queue

    def dequeue(self):
        if len(self.queue) > 0:
            temp = self.queue[-1]
            #self.queue.pop(-1)
            self.queue = self.queue[0:-1]
            return temp

    def rear(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def front(self):
        return self.queue[-1]

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    myStack = Stack()
    myStack.push(42)
    myStack.push(30)
    myStack.push(20)
    print("Top of stack: ", myStack.top())
    print("Size of stack: ", myStack.size())
    popped_value = myStack.pop()
    print("Popped value: ", popped_value)

    print("Top of stack: ", myStack.top())
    print("Size of stack: ", myStack.size())
    min = myStack.min()
    print("Min value: ", min)
    print()

    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print("Size of queue: ", myQueue.size())
    print("Front of queue: ", myQueue.front())
    print("Rear of queue: ", myQueue.rear())
    dequeuedItem = myQueue.dequeue()
    print("Dequeue item: ", dequeuedItem)

    print("Front of queue: ", myQueue.front())
    print("Rear of queue: ", myQueue.rear())
