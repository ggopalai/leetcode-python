# concurrency, pair synchronization
class Foo:
    def __init__(self):
        self.firstJobDone = False
        self.secondJobDone = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.firstJobDone = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        # wait for firstJob to complete
        while not self.firstJobDone:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.secondJobDone = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        # wait for second job to complete
        while not self.secondJobDone:
            continue
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
