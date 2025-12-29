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


class Solution:
    def middleNode_old(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr = head

        while curr:
            len += 1
            curr = curr.next

        for _ in range(len // 2):
            head = head.next

        return head

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
