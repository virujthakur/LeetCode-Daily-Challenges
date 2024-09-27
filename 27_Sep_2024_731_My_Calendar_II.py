#TC: O(N^2) SC: O(N)
class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.events_double_booked = []

    def book(self, start: int, end: int) -> bool:
        def intersect(p1, p2):
            p1,p2 = min(p1, p2), max(p1, p2)
        
            st1, en1 = p1
            st2, en2 = p2
            
            if en1 <= st2:
                return False
            else:
                return True
            
        def get_double_booked_time(p1, p2):
            p1,p2 = min(p1, p2), max(p1, p2)
            
            return tuple((max(p1[0], p2[0]), min(p1[1], p2[1])))
            
        
        for e in self.events_double_booked:
            if intersect(e, (start, end)):
                return False
            
        for e in self.events:
            if intersect(e, (start,end)):
                self.events_double_booked.append(get_double_booked_time(e, (start,end)))
        
            
        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
