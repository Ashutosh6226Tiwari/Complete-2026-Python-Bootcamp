import heapq

heap = []  # start with an empty list, which will act as our heap

# push elements into the heap
heapq.heappush(heap, 10)  # add 10 → heap = [10]
heapq.heappush(heap, 5)   # add 5 → heap = [5, 10] (min-heap keeps smallest at front)
heapq.heappush(heap, 20)  # add 20 → heap = [5, 10, 20]
heapq.heappush(heap, 2)   # add 2 → heap = [2, 5, 20, 10]

print(heap)  # prints the internal heap list (not sorted, but heap-structured)




import heapq

numbers = [8, 3, 10, 1, 5, 2]

# Turn the list into a valid min-heap in place
heapq.heapify(numbers)

print(numbers)       # internal heap structure (not sorted, but heap property maintained)
print(numbers[0])    # smallest element in the heap (root)

# Pop elements one by one (always removes the smallest)
print(heapq.heappop(numbers))  # removes 1
print(heapq.heappop(numbers))  # removes 2
print(heapq.heappop(numbers))  # removes 3

print(numbers)       # remaining heap after pops
