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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy

        while list1 and list2:
            if list1.val > list2.val:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next

            result = result.next

        result.next = list1 or list2

        return dummy.next


print(
    Solution().mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4])),
    [1, 1, 2, 3, 4, 4],
)
print(Solution().mergeTwoLists(build_list([]), build_list([])), [])
print(Solution().mergeTwoLists(build_list([]), build_list([0])), [0])
print(Solution().mergeTwoLists(build_list([0]), build_list([])), [0])
