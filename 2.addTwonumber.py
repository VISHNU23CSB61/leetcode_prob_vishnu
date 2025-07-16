class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node = l1
        l2_node = l2
        new_head = ListNode()
        res = new_head
        increment = 0
        while l1_node is not None or l2_node is not None:
            l1_val = l1_node.val if l1_node is not None else 0
            l2_val = l2_node.val if l2_node is not None else 0
            num = l1_val + l2_val + increment
            increment = 0
            if num >= 10:
                num -= 10
                increment = 1
            new_node = ListNode(num)
            res.next = new_node
            res = res.next
            l1_node = l1_node.next if l1_node is not None else None
            l2_node = l2_node.next if l2_node is not None else None
        if increment == 1:
            new_node = ListNode(1)
            res.next = new_node
            res = res.next
        return new_head.next
