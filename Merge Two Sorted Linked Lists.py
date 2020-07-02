class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, one, two):
        """
        input: ListNode one, ListNode two
        return: ListNode
        """
        # write your solution here
        if one is None:
            return two
        elif two is None:
            return one
        currNode_1 = one
        currNode_2 = two
        fakeHead = ListNode(None)
        prevNode = fakeHead
        while currNode_1 is not None and currNode_2 is not None:
            if currNode_1.val <= currNode_2.val:
                currNode = currNode_1
                currNode_1 = currNode_1.next
            else:
                currNode = currNode_2
                currNode_2 = currNode_2.next
            prevNode.next = currNode
            prevNode = currNode
        if currNode_1 is None:
            prevNode.next = currNode_2
        else:
            prevNode.next = currNode_1
        return fakeHead.next


"""    
Node0 = ListNode(7)
Node1 = ListNode(7)
Node2 = ListNode(8)
Node0.next = Node1
Node1.next = Node2

Node3 = ListNode(1)
Node4 = ListNode(7)
Node5 = ListNode(9)
Node3.next = Node4
Node4.next = Node5
"""
Node0 = Node3 = None
ans = Solution()
a = ans.merge(Node0, Node3)