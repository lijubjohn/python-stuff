class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
A node can be added in three ways
1) At the front of the linked list
2) After a given node.
3) At the end of the linked list.
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    #  insert a new node at the beginning
    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Appends a new node at the end
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(data)

    # delete node based on value comparison
    def delete(self, data):
        tmp = self.head

        if not tmp and tmp.data == data:
            self.head = tmp.next
            return
        while tmp:
            if (tmp.data == data):
                break
            prev = tmp
            tmp = tmp.next

        if not tmp:
            return
        prev.next = tmp.next

    # traverse list
    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end="")
            tmp = tmp.next
            if tmp:
                print("->", end="")


if __name__ == '__main__':
    llist = LinkedList()
    # llist.append(Node(1))
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.print()
    print("")
    llist.delete(3)
    llist.print()
