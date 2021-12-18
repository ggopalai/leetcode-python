Stacks in Python can be implemented using the following structures - 
1. List - append(), pop() 
2. collections.deque - append(), pop()
3. queue.LifoQueue - put(), get()


1. Lists might have time issues once number of elements grow. This is because, elements need to be stored next to each other. However, once a block of memory is full, it takes time to find the next block of memory. 

2. Implemented using a double-linked-list. Fast, but not thread safe. 

3. Threadsafe.