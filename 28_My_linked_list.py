class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


class MyLinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def addFirst(self, val_f):
        self.root = Node(value=val_f, _next=None)
        self.length = 0

    def get_index_item(self, index_el):
        cnt = 0
        result_el = self.root
        while cnt < index_el:
            result_el = result_el._next
            cnt += 1
        return result_el

    def change_next(self, method, index_for_change, val):
        if self.root is None:
            self.addFirst(val_f=val)
        elif method == "add":
            if index_for_change == 0:
                self.root = Node(value=val, _next=self.get_index_item(index_el=0))
            elif index_for_change <= self.length:
                self.get_index_item(index_el=index_for_change - 1)._next = Node(
                    value=val, _next=self.get_index_item(index_el=index_for_change)
                )
            else:
                self.get_index_item(index_el=self.length)._next = Node(value=val)
            self.length += 1
        elif method == "subtract":
            self.get_index_item(
                index_el=index_for_change - 1
            )._next = self.get_index_item(index_el=index_for_change)._next
            self.length -= 1

    def addAtTail(self, val_t):
        self.change_next(method="add", index_for_change=self.length + 1, val=val_t)

    def addAtHead(self, val_h):
        self.change_next(method="add", index_for_change=0, val=val_h)

    def addAtIndex(self, index_add, val_add):
        self.change_next(method="add", index_for_change=index_add, val=val_add)

    def deleteAtIndex(self, index_sub):
        self.change_next(method="subtract", index_for_change=index_sub, val=None)

    def get(self, index):
        return self.get_index_item(index_el=index).value

