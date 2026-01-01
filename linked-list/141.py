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


def build_list(values: list) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("True")
                return True

        print("False")
        return False


node_1_4 = ListNode(5)
node_1_3 = ListNode(4, node_1_4)
node_1_2 = ListNode(3, node_1_3)
node_1_1 = ListNode(2, node_1_2)
node_1_0 = ListNode(1, node_1_1)
# node_1_3.next = node_1_1
Solution().hasCycle(node_1_0)
