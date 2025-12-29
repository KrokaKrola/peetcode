from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    reversed = None

    while head:
        reversed_new_head = ListNode(head.val, reversed)
        reversed = reversed_new_head
        head = head.next

    return reversed


def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


# =========================
node_1_3 = ListNode(3)
node_1_2 = ListNode(2, node_1_3)
node_1_1 = ListNode(1, node_1_2)
print("before reverse", node_1_1)
res1 = reverseList2(node_1_1)
print("after reverse", res1)

# =========================
node_2_2 = ListNode(2)
node_2_1 = ListNode(1, node_2_2)
print("before reverse", node_2_1)
res2 = reverseList2(node_2_1)
print("after reverse", res2)
