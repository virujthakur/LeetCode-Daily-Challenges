#SC: O(N)
class CustomStack:

    def __init__(self, maxSize: int):
        self.st =[]
        self.sz = maxSize
    
    #TC: O(1)
    def push(self, x: int) -> None:
        if len(self.st) < self.sz:
            self.st.append(x)
    #TC: O(1)
    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        return self.st.pop()
    #TC: O(K)
    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.st),k)):
            self.st[i]+= val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
