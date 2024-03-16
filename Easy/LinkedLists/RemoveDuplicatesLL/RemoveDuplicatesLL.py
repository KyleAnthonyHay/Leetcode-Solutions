# Optimal Solution

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedList
