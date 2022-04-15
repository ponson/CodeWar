class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    lens = 0
    if not node:
        return 0
    else:
        lens += 1
    while node.next is not None:
        lens += 1
        node = node.next

    return len


def count(node, data):
    counts = 0
    if not node:
        return counts

    while node:
        if node.data == data:
            counts += 1
        node = node.next

    return counts
