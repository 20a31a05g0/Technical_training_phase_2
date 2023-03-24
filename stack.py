class Stack:
    def __init__(self):
        self.arr=[]
        self.size=5
    def push(self,element):
        if len(self.arr)>=5:
            print('stack is full')
        else:
            self.arr.append(element)
    def pop(self):
        if len(self.arr)==0:
            print('stack is empty')
        else:
            return self.arr.pop()
    def peek(self):
        if len(self.arr)==0:
            print('stack is empty')
        else:
            print(self.arr[-1])
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=Stack()
s.pop()
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.pop()
s.peek()
print(s.arr)
r=Stack()
r.push(s.pop())
r.push(s.pop())
r.push(s.pop())
r.push(s.pop())
print(r.arr)


