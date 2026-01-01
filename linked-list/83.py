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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# l_l = build_list([1, 1, 2])
# print(Solution().deleteDuplicates(l_l), "= 1 -> 2")

# l_l = build_list([1, 1, 2, 3, 3])
# print(Solution().deleteDuplicates(l_l), " = 1 -> 2 -> 3")

l_l = build_list([1, 1, 1])
print(Solution().deleteDuplicates(l_l), " = 1")
