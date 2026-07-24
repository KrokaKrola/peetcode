from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next if fast is not None else None

        while fast:
            fast = fast.next
            slow = slow.next if slow is not None else None

        slow.next = slow.next.next

        return dummy.next


l_l = build_list([1, 2, 3, 4, 5])
print(Solution().removeNthFromEnd(l_l, 2))

l_l = build_list([1])
print(Solution().removeNthFromEnd(l_l, 1))

l_l = build_list([1, 2])
print(Solution().removeNthFromEnd(l_l, 1))

l_l = build_list([1, 2])
print(Solution().removeNthFromEnd(l_l, 2))
