# Queue -> FIFO (First In First Out)

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        item = self.queue[0]
        del self.queue[0]
        return item

    def peek(self):
        return self.queue[0]

    def sizeOfQueue(self):
        return len(self.queue)

    def queueShow(self):
        return self.queue

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Queue: ", queue.queueShow())
print("Size of Queue: ", queue.sizeOfQueue())
print("Peek Value: ", queue.peek())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Size of Queue: ", queue.sizeOfQueue())
print("Peek Value: ", queue.peek())
print("Queue: ", queue.queueShow())
