from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.events = SortedList()
        
    def book(self, start: int, end: int) -> bool:
        i = bisect_right(self.events, (start, end))
        if i > 0 and self.events[i - 1][1] > start or i < len(self.events) and self.events[i][0] < end:
            return False

        self.events.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)