
class LinkedListNode:
    # https://www.python.org/dev/peps/pep-0484/#forward-references
    def __init__(self, val, next_node: 'LinkedListNode' = None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f"LinkedListNode: {self.val}"


class LinkedList:

    def push(self, val):
        


    def __init__(self):
        self.head = None
        self.tail = None
        return None

    def __repr__(self):
        node = self.head
        nodes = []
        while node.next is not None:
            nodes.append(node.val)
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node.next is not None:
            yield node.val
