class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insert(self, head, value):
        """
        input: ListNode head, int value
        return: ListNode
        """
        # write your solution here
        newNode = ListNode(value)
        if not head:
            head = newNode
            return head
        fakeHead = ListNode(None)
        fakeHead.next = head
        prevNode = fakeHead
        currNode = head
        while True:
            if prevNode == fakeHead and value <= currNode.val:
                prevNode.next = newNode
                newNode.next = currNode
                return fakeHead.next
            prevNode = currNode
            currNode = currNode.next
            if not currNode:
                prevNode.next = newNode
                newNode.next = currNode
                return fakeHead.next
            if value >= prevNode.val and value < currNode.val:
                prevNode.next = newNode
                newNode.next = currNode
                return fakeHead.next


Node0 = ListNode(6)
Node1 = ListNode(7)
Node2 = ListNode(9)
Node0.next = Node1
Node1.next = Node2
ans = Solution()
a = ans.insert(Node0, 10)