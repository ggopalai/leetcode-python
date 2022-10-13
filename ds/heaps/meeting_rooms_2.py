import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) #sort by start times
        
        rooms = [] #represents rooms
        
        heapq.heappush(rooms, intervals[0][1]) #allocate first meeting to room
        
        for i in range(1, len(intervals)):
            
            #if start time of meeting is after the end-time of meeting with least time, remove existing meeting
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            
            #allocating meeting room
            heapq.heappush(rooms, intervals[i][1])
        
        return len(rooms)
            