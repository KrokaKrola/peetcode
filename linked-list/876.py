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

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            head = head.next

        return head


node_1_4 = ListNode(5)
node_1_3 = ListNode(4, node_1_4)
node_1_2 = ListNode(3, node_1_3)
node_1_1 = ListNode(2, node_1_2)
node_1_0 = ListNode(1, node_1_1)
res1 = Solution().middleNode2(node_1_0)
print("after ", res1)
