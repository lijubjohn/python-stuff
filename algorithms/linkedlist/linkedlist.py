"""
Pros
Linked Lists have constant-time insertions and deletions in any position,
in comparison, arrays require O(n) time to do the same thing.
Linked lists can continue to expand without having to specify
their size ahead of time (remember our lectures on Array sizing
form the Array Sequence section of the course!)

Cons
To access an element in a linked list, you need to take O(k) time
to go from the head of the list to the kth element.
In contrast, arrays have constant time operations to access
elements in an array.
"""


class SinglyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)