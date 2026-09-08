# Build a Linked List Node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create Node objects
node1 = Node(10)
node2 = Node(20)

# link node1 to node2
node1.next = node2

print(node1.data)        # 10
print(node1.next.data)   # 20
print(node1.next.next)



# But a real Linked List may contain 100 or 1000 nodes, so we need a loop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# link them: 10 → 20 → 30 → None
node1.next = node2
node2.next = node3

# traverse and print
current = node1
while current is not None:
    print(current.data)
    current = current.next
