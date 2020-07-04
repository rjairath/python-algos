class Stack():
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        n = len(self.arr)
        x = self.arr[n-1]
        self.arr.pop()
        return x

    def peek(self):
        n = len(self.arr)
        return self.arr[n-1]


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.peek())
print(s.pop())
