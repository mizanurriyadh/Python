# Stack -> LIFO (Last In Fast Out)

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def peek(self):
        return self.stack[-1]

    def sizeOfStack(self):
        return len(self.stack)

    def stackShow(self):
        return self.stack


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)


print("Stack: ", stack.stackShow())
print("Size of Stack: ",stack.sizeOfStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())

print("Peek: ", stack.peek())


print("Size of Stack: ", stack.sizeOfStack())
print("Stack: ", stack.stackShow())