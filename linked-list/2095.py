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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        slow = prev
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return prev.next

    def deleteMiddle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return head


# =========================
l1 = build_list([1, 3, 4, 7, 1, 2, 6])
print("before", l1)
l1 = Solution().deleteMiddle2(l1)
print("after ", l1)
print("---------")

l2 = build_list([1])
print("before", l2)
l2 = Solution().deleteMiddle2(l2)
print("after ", l2)
print("---------")
