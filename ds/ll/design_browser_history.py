class Node:
    """
    Doubly linked-list node.
    """
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Open the homepage.
        """
        self.cursor = Node(homepage)

    # add new node 
    def visit(self, url: str) -> None:
        """
        Deletes all history in the front and visits new website.
        """
        newNode = Node(url)
        newNode.prev = self.cursor
        self.cursor.next = newNode
        self.cursor = newNode

    # move one step back 
    def back(self, steps: int) -> str:
        """
        Move 'steps' number of steps back, if available, else till the beginning.
        """
        while self.cursor.prev and steps:
            self.cursor = self.cursor.prev
            steps -= 1

        return self.cursor.val
    
    # move one step front 
    def forward(self, steps: int) -> str:
        """
        Move 'steps' number of steps back, if available, else till the end.
        """
        while self.cursor.next and steps:
            self.cursor = self.cursor.next
            steps -= 1
        
        return self.cursor.val
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)