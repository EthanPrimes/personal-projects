# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        root_node = ListNode()
        next_node = root_node
        while True:
            total = carry
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            digit, carry = total % 10, total // 10
            next_node.val = digit

            if not ((l1 and l1.next) or (l2 and l2.next) or carry):
                return root_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            next_node.next = ListNode()
            next_node = next_node.next

def construct_list(nums):
    root_node = ListNode()
    next_node = root_node
    for index, elt in enumerate(nums):
        next_node.val = elt
        next_node.next = ListNode()
        if index != len(nums) - 1:
            next_node = next_node.next

    return root_node

if __name__ == "__main__":
    l1 = construct_list([9] * 7)
    l2 = construct_list([9] * 4)
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    print(type(res))
    while res:
        print(res.val)
        res = res.next
