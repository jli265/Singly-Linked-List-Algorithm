class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeSort(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        length = self.size(head)
        if length <= 1:
            return head
        fakeHead = ListNode(None)
        fakeHead.next = head
        for i in range(length - 1):
            curr1 = fakeHead
            curr2 = fakeHead.next
            curr3 = fakeHead.next.next
            curr4 = fakeHead.next.next.next
            for j in range(length - i - 1):
                if curr2.val > curr3.val:
                    curr1.next = curr3
                    curr2.next = curr4
                    curr3.next = curr2
                    curr1 = curr3
                    curr3 = curr4
                    if curr4 is not None:
                        curr4 = curr4.next
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
                    curr3 = curr3.next
                    if curr4 is not None:
                        curr4 = curr4.next
        return fakeHead.next

    def size(self, head):
        sum = 0
        while head is not None:
            head = head.next
            sum += 1
        return sum


'''
Node0 = ListNode(9)
Node1 = ListNode(7)
Node2 = ListNode(6)
Node0.next = Node1
Node1.next = Node2
'''
Node0 = ListNode(None)
Node0.next = None
ans = Solution()
a = ans.mergeSort(Node0)