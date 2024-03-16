# Optimal Solution

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slow = linkedList
    fast = linkedList
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == None:
            return slow

    return slow
