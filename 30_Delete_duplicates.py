class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


nd1 = Node(value="1")
nd2 = Node(value="2")
nd3 = Node(value="3")
nd4 = Node(value="3")
nd5 = Node(value="5")

nd1._next = nd2
nd2._next = nd3
nd3._next = nd4
nd4._next = nd5
nd5._next = None


def print_func(g_root):
    head = g_root
    while head:
        print(head.value)
        head = head._next


def del_dup(root):
    """
    This function deletes duplicates in sorted linked list
    """
    head = root
    while head._next:
        if head.value == head._next.value:
            head._next = head._next._next
        else:
            head = head._next


print_func(nd1)
del_dup(nd1)
print_func(nd1)