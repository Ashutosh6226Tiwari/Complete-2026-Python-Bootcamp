# mannual version
'''You manually created a linked list:
10 → 20 → 30 → None

Then you used a while loop to traverse and print each node.'''

class Node:
    def __init__(self, data):
        self.data = data        # store the value inside this node
        self.next = None        # pointer to the next node (initially None)


# Create three nodes manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them together: node1 → node2 → node3
node1.next = node2
node2.next = node3

# Start traversal from the first node
current = node1

# Traverse until current becomes None (end of list)
while current is not None:
    print(current.data)        # print the value of the current node
    current = current.next     # move to the next node


# <------------------------------------------------------------------------------------------------>
# Now create a LinkedList class instead of manually managing node1, node2, etc.

class Node:
    def __init__(self, data):
        self.data = data        # store the value inside this node
        self.next = None        # pointer to the next node (initially nothing)


class linkedlist:
    def __init__(self):
        self.head = None        # start with an empty linked list

    def display(self):
        current = self.head     # begin at the head node
        while current is not None:     # traverse until the end of the list
            print(current.data)        # print the value of the current node
            current = current.next     # move to the next node


# Create three nodes manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them together: node1 → node2 → node3
node1.next = node2
node2.next = node3

# Create a linked list and attach node1 as the head
ll = linkedlist()
ll.head = node1

# Display the linked list
ll.display()   # Output: 10 20 30

# <----------------------------------------------------------------------------------------------->
# Exercise 6 — Create insert()

class Node:
    def __init__(self, data):
        self.data = data        # store the value inside the node
        self.next = None        # pointer to the next node (initially empty)


class linkedlist:
    def __init__(self):
        self.head = None        # start with an empty linked list

    def insert(self, data):
        new_node = Node(data)   # create a new node with given data

        # Case 1: if list is empty → new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: otherwise traverse to the last node
        current = self.head
        while current.next is not None:   # move forward until last node
            current = current.next

        current.next = new_node           # attach new node at the end

    def display(self):
        current = self.head               # start from the head
        while current is not None:        # traverse until end of list
            print(current.data)           # print each node's value
            current = current.next        # move to next node


# Create a linked list and insert values
ll = linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()   # prints: 10 20 30


# <----------------------------------------------------------------------------------------------->

# Add a method:
# def search(self, target):
# It should return True if the target exists and False otherwise

class Node:
    def __init__(self, data):
        self.data = data        # store the value
        self.next = None        # pointer to the next node


class linkedlist:
    def __init__(self):
        self.head = None        # start with an empty list

    def insert(self, data):
        new_node = Node(data)   # create a new node

        # Case 1: if list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: otherwise traverse to the last node
        current = self.head
        while current.next is not None:   # move until last node
            current = current.next

        current.next = new_node           # attach new node at the end

    def search(self, target):
        current = self.head               # start from head
        while current is not None:        # traverse entire list
            if current.data == target:    # check if value matches
                return True               # found
            current = current.next        # move to next node
        return False                      # not found

    def display(self):
        current = self.head               # start from head
        while current is not None:        # traverse list
            print(current.data)           # print each node's data
            current = current.next        # move to next node


# Create list and insert values
ll = linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(30)

# Search examples
print(ll.search(20))  # True
print(ll.search(50))  # False

    
    
