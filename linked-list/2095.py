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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        slow = prev
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return prev.next


# =========================
node_1_6 = ListNode(6)
node_1_5 = ListNode(2, node_1_6)
node_1_4 = ListNode(1, node_1_5)
node_1_3 = ListNode(7, node_1_4)
node_1_2 = ListNode(4, node_1_3)
node_1_1 = ListNode(3, node_1_2)
node_1_0 = ListNode(1, node_1_1)
print("before", node_1_0)
res1 = Solution().deleteMiddle(node_1_0)
print("after ", res1)
