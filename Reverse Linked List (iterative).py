class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        if head is None or head.next is None:
            return head
        initTail = self.oneBeforeTail(head).next
        while head.next is not None:
            Node = self.oneBeforeTail(head)
            currTail = Node.next
            Node.next = None
            currTail.next = Node
        return initTail

    def oneBeforeTail(self, head):
        while head.next.next is not None:
            head = head.next
        return head


Node0 = ListNode(8)
Node1 = ListNode(7)
Node2 = ListNode(6)
Node0.next = Node1
Node1.next = Node2
ans = Solution()
ans.reverse(Node0)

