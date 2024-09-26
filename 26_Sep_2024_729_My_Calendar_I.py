class MyCalendar:
    #TC: O(N^2) SC: O(N)
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        
        def intersect(p1, p2):
            st1, en1 = p1
            st2, en2 = p2
            
            if en1 <= st2:
                return False
            else:
                return True
        
        for e in self.events:
            p1= min(e, (start,end))
            p2= max(e, (start,end))
            
            if intersect(p1, p2):
                return False
            
        self.events.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
