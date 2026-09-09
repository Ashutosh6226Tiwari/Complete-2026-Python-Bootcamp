from collections import deque

# create empty deque
dq = deque()

# append to the right (default)
dq.append(10)       # dq = [10]
dq.append(20)       # dq = [10, 20]
dq.append(30)       # dq = [10, 20, 30]

# append to the left
dq.appendleft(5)    # dq = [5, 10, 20, 30]

# remove from the right (stack behavior)
dq.pop()            # removes 30 → dq = [5, 10, 20]

# remove from the left (queue behavior)
dq.popleft()        # removes 5 → dq = [10, 20]

# peek at elements
print(dq[0])        # first element → 10
print(dq[-1])       # last element → 20

# extend with multiple elements
dq.extend([40, 50])     # dq = [10, 20, 40, 50]
dq.extendleft([2, 1])   # dq = [1, 2, 10, 20, 40, 50]

# rotate elements
dq.rotate(1)        # dq = [50, 1, 2, 10, 20, 40]
dq.rotate(-2)       # dq = [2, 10, 20, 40, 50, 1]
