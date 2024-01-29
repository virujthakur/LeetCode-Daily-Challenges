from collections import deque
'''
push : TC: O(1) SC:O(1)
pop : TC: O(N) SC:O(N)
peek : TC: O(N) SC:O(N)
empty : TC: O(1) SC:O(1)

'''
class MyQueue:

    def __init__(self):
        self.st1= deque()
        self.st2= deque()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        while self.st1:
            self.st2.append(self.st1[-1])
            self.st1.pop()
        val = self.st2[-1]
        self.st2.pop()
        
        while self.st2:
            self.st1.append(self.st2[-1])
            self.st2.pop()
        return val

    def peek(self) -> int:
        while self.st1:
            self.st2.append(self.st1[-1])
            self.st1.pop()
        val = self.st2[-1]
        
        while self.st2:
            self.st1.append(self.st2[-1])
            self.st2.pop()
        return val

    def empty(self) -> bool:
        return len(self.st1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
