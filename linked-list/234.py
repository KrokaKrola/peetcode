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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


l1 = build_list([1, 2, 2, 1])
print(Solution().isPalindrome(l1), True)
l1 = build_list([1, 2])
print(Solution().isPalindrome(l1), False)
l1 = build_list([])
print(Solution().isPalindrome(l1), True)
l1 = build_list([1, 2, 1])
print(Solution().isPalindrome(l1), True)
l1 = build_list([1, 2, 3])
print(Solution().isPalindrome(l1), False)
