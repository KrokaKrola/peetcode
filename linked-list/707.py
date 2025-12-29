class Node:
    def __init__(self, value=0, next=None):
        self.next = next
        self.value = value


class MyLinkedList:
    head: Node = None

    def __init__(self):
        print()

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        it = 0

        current = self.head
        while current:
            if it == index:
                return current.value
            current = current.next
            it += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val, None)

        if not self.head:
            self.head = new_tail
        else:
            current = self.head

            while current:
                if not current.next:
                    current.next = new_tail
                    break
                current = current.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            new_node = Node(val, self.head)
            self.head = new_node
            return

        it = 0

        current = self.head
        while current:
            if it == index - 1:
                new_node = Node(val)
                old_next = current.next
                new_node.next = old_next
                current.next = new_node
                break
            current = current.next
            it += 1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        it = 0

        current = self.head
        while current:
            if it == index - 1 and current.next:
                current.next = current.next.next
                break
            current = current.next
            it += 1

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)


myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# print(myLinkedList)
# myLinkedList.addAtTail(3)
# print(myLinkedList)
# myLinkedList.addAtIndex(1, 2)
# print(myLinkedList)
# print(myLinkedList.get(1))
# myLinkedList.deleteAtIndex(1)
# print(myLinkedList)
# print(myLinkedList.get(1))

myLinkedList.addAtIndex(0, 10)
print(myLinkedList)
myLinkedList.addAtIndex(0, 20)
print(myLinkedList)
myLinkedList.addAtIndex(1, 30)
print(myLinkedList)
myLinkedList.get(0)
