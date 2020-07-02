class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
  def checkCycle(self, head):
    """
    input: ListNode head
    return: boolean
    """
    # write your solution here
    initNode=head
    if head==None or head.next==None:
      return False
    while head.next is not None:
      if head.next==initNode:
        return True
      head=head.next
    return False

Node0 = ListNode(6)
Node1 = ListNode(7)
Node2 = ListNode("a")
Node0.next = Node1
Node1.next = Node2
Node2.next=Node0
ans=Solution()
a=ans.checkCycle(Node0)