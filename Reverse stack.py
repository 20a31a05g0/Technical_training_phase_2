class Stack():
    def __init__(self):
        self.arr=[]
        self.temp=[]
        self.temp1=[]
    def push(self,ele):
        self.arr.append(ele)   
    def pop(self):
        if len(self.arr)==0:
            print('stack underflow')
        else:
            self.arr.pop()
    def isempty():
        if len(self.arr)==0:
            return True
        else:
            return False
    def print_stack(self):
        mid=len(self.arr)//2
        for i in range(mid):
            self.temp.append(self.arr.pop())
        for i in range(len(self.arr)):
            self.temp1.append(self.arr.pop())
        for i in range(mid):
            self.temp1.append(self.temp.pop())
        print(self.temp1)

s=Stack()
s.pop()
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
s.pop()
s.print_stack()
