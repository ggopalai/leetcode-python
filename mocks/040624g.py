'''Given an array intervals where intervals[i] = [li, ri] represent 
the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

'''
from typing import List

def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: [x[0], -x[1]])
    j = 0
    count = 0
    n = len(intervals)
    while j < n - 1:
        i = j + 1 
        while i < n and intervals[i][1] <= intervals[j][1]:
            count += 1
            i += 1
        j = i
    
    return n - count
        
    # ans = 1
    # intervals.sort(key = lambda x: (x[0], -x[1]))
    # prev_end = intervals[0][1]
    # for start, end in intervals:
    #     if end > prev_end:
    #         ans += 1
    #         prev_end = end
    # return ans


assert removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2
assert removeCoveredIntervals([[1,4],[2,3]]) == 1
assert removeCoveredIntervals([[3,10],[4,10],[5,11]]) == 2
assert removeCoveredIntervals([[1,2],[1,4],[3,4]]) == 1


'''
You have a browser of one tab where you start on the homepage and you can
visit another url, get back in the history number of steps or move forward 
in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

void visit(string url) Visits url from the current page. It clears up all the forward history.

string back(int steps) Move steps back in history. If you can only return x 
steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.

string forward(int steps) Move steps forward in history. If you can only forward x steps 
in the history and steps > x, you will forward only x steps. Return the current url after 
forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.cur + 1]
        self.arr.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        idx = max(0, self.cur - steps)
        self.cur = idx
        return self.arr[idx]

    def forward(self, steps: int) -> str:
        n = len(self.arr)
        idx = min(n - 1, self.cur + steps)
        self.cur = idx 
        return self.arr[idx]