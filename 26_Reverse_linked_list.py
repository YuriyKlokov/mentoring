class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


def my_reverse(head):
    """
    This function reverses links in linked list
    linked list should be done wiht link as the folows: _next='nd2', _next='nd2', _next='nd3' etc
    @head:  first item of the lined list
    ------------------
    examples: [1] -> [2] -> [3] -> None
              None <- [1] <- [2] <- [3]
    """

    cnt = head
    dct = {head: None}
    link = "nd1"
    while cnt._next != None:
        cnt = eval(cnt._next)
        dct[cnt] = link
        link = link[:2] + str(int(link[2:]) + 1)
    for k, v in dct.items():
        k._next = v


nd1 = Node(value="a", _next="nd2")
nd2 = Node(value="b", _next="nd3")
nd3 = Node(value="c", _next="nd4")
nd4 = Node(value="d", _next=None)

print(nd1._next)
print(nd2._next)
print(nd3._next)
print(nd4._next)

my_reverse(nd1)

print(nd1._next)
print(nd2._next)
print(nd3._next)
print(nd4._next)

