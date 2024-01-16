class RandomizedSet:
    #TC : O(1) SC: O(N)
    def __init__(self):
        self.idx = defaultdict(lambda: -1)
        self.l= []

    def insert(self, val: int) -> bool:
        if self.idx[val] == -1:
            self.idx[val] = len(self.l)
            self.l.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.idx[val] != -1 and len(self.l)> 0:
            le= self.l[-1]
            self.idx[le]= self.idx[val]
            self.l[self.idx[val]]= le
            self.l.pop()
            self.idx[val]= -1
            return True
        return False
        

    def getRandom(self) -> int:
        if len(self.l)>0:
            idi = random.randint(0,len(self.l)-1)
            #print(idi, len(self.l))
            return self.l[idi]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
