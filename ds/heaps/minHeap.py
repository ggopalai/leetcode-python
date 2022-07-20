import heapq

minHeap = []

heapq.heapify(minHeap)

heapq.heappush(minHeap, 10)
heapq.heappush(minHeap, 20)
heapq.heappush(minHeap, 0)

print(str(minHeap))

heapq.heappop(minHeap)

print(str(minHeap))

min = minHeap[0]

print(min)

