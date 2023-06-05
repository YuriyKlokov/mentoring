class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


nd1 = Node(value="1")
nd2 = Node(value="2")
nd3 = Node(value="3")
nd4 = Node(value="4")
nd5 = Node(value="5")

nd1._next = nd2
nd2._next = nd3
nd3._next = nd4
nd4._next = nd5
nd5._next = None


def find_middle(head):
    """
    This function finds middle element of a linked list.
    If list lenght is even function returns the right element.
    @head - linked list root element
    @middle_el - middle element
    """

    current_el = head
    middle_el = head
    cnt = 1
    while current_el:
        if cnt % 2 == 0:
            middle_el = middle_el._next
        cnt += 1
        current_el = current_el._next
    return middle_el


find_middle(nd1).value

