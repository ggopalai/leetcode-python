import heapq

#[1,2,3]

maxHeap = list()

heapq.heapify(maxHeap)

heapq.heappush(maxHeap, -1)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -3)

print(str(maxHeap))

max = maxHeap[0] * -1
print(max)

heapq.heappop(maxHeap)

print(str(maxHeap))

heapq.heappush(maxHeap, 10 * -1)

print(str(maxHeap))
